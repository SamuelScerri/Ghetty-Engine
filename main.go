package main

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"

	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

var Cores = 1

const Width, Height = 320, 180
const FOV = 90

const Near, Far = .1, 1000
const Aspect = 16 / 9

var TileXSize, TileYSize = Width, Height

var Tiles [4][3]Tile
var Buffer []byte = make([]byte, Width*Height*4)

var Triangles []Triangle

type Game struct{}

func BasicShader(s, t, w float32) (r, g, b float32) {
	r = s
	g = t
	b = w

	return
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (screenWidth, screenHeight int) {
	return Width, Height
}

func (g *Game) Update() error {
	return nil
}

var Position Vertex = Vertex{0, 0, 15, 0}
var Projection Matrix = ProjectionMatrix()

func (g *Game) Draw(screen *ebiten.Image) {

	if ebiten.IsKeyPressed(ebiten.KeyRight) {
		Position[X] += .125 / 2 / 2
	}

	if ebiten.IsKeyPressed(ebiten.KeyLeft) {
		Position[X] -= .125 / 2 / 2
	}

	var matrix Matrix = TransformationMatrix(Position, Vertex{0, 0, 0, 1})
	matrix = matrix.Multiply(&Projection)

	var trianglesPerCore int = len(Triangles) / Cores

	WaitGroup.Add(Cores)

	for i := 0; i < Cores; i++ {
		go func(offset int) {
			for p := offset; p < offset+trianglesPerCore; p++ {
				var copiedTriangle Triangle = Triangles[p].Copy()
				copiedTriangle.Transform(&matrix)

				var processedTriangles []ProcessedTriangle = BuildAndProcess(&copiedTriangle)

				for _, triangle := range processedTriangles {
					var xMin, yMin, xMax, yMax int = triangle.TileBoundary(&Tiles)

					for y := yMin; y < yMax; y++ {
						for x := xMin; x < xMax; x++ {
							Mutex.Lock()
							Tiles[x][y].Add(&triangle)
							Mutex.Unlock()
						}
					}
				}
			}

			WaitGroup.Done()
		}(trianglesPerCore * i)
	}

	WaitGroup.Wait()

	WaitGroup.Add(Cores)

	for y := range Tiles[0] {
		for x := range Tiles {
			go func(x, y int) {
				Tiles[x][y].Clear(byte(x+y)*4, byte(x+y)*4, byte(x+y)*4)
				Tiles[x][y].Rasterize()

				WaitGroup.Done()
			}(x, y)
		}
	}

	WaitGroup.Wait()

	screen.WritePixels(Buffer)
	ebitenutil.DebugPrint(screen, "FPS: "+strconv.Itoa(int(ebiten.ActualFPS())))
}

func main() {
	fmt.Println("Please Select Triangle Rasterization Algorithm:")

	fmt.Println("")

	fmt.Println("1: Sweep-Line Algorithm")
	fmt.Println("2: Barycentric Algorithm")
	fmt.Println("3: Edge Test Algorithm")

	fmt.Println("")

	reader := bufio.NewReader(os.Stdin)
	algorithm, _, _ := reader.ReadRune()

	var i int

	switch algorithm {
	case '1':
		AlgorithmUsed = SweepLineAlgorithm
	case '2':
		AlgorithmUsed = BarycentricAlgorithm
	case '3':
		AlgorithmUsed = EdgeTestAlgorithm
	}

	fmt.Println("")

	fmt.Print("Please Type How Many Cores Will Be Utilized: ")

	fmt.Scan(&Cores)

	fmt.Print("Please Type How Cores Will Be Divided Per Row: ")

	fmt.Scan(&i)
	TileXSize /= i

	fmt.Print("Please Type How Cores Will Be Divided Per Column: ")

	fmt.Scan(&i)
	TileYSize /= i

	for y := range Tiles[0] {
		for x := range Tiles {
			Tiles[x][y].X = x * TileXSize
			Tiles[x][y].Y = y * TileYSize
			Tiles[x][y].Frame = Buffer
		}
	}

	for i := 0; i < 12; i++ {
		var triangle Triangle = Triangle{
			Vertices: [3]Vertex{
				{0, -.25, 0, 1},
				{-.25, .5, 0, 1},
				{.25, .25, 0, 1},
			},
		}

		var matrix Matrix = TransformationMatrix(Vertex{rand.Float32()*4 - 2, rand.Float32()*4 - 2, -20, 0}, Vertex{0, 0, 0, 0})
		triangle.Transform(&matrix)
		triangle.Shader = BasicShader
		Triangles = append(Triangles, triangle)
	}

	ebiten.SetWindowSize(Width*2, Height*2)
	ebiten.SetWindowTitle("Ghetty Engine")
	ebiten.SetTPS(ebiten.SyncWithFPS)
	ebiten.SetScreenClearedEveryFrame(false)
	ebiten.SetVsyncEnabled(true)

	if err := ebiten.RunGame(&Game{}); err != nil {
		log.Fatal(err)
	}
}
