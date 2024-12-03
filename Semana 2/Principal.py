using System;

namespace FigurasGeometricas
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear un círculo con radio de 5 unidades
            Circulo circulo = new Circulo(5);
            Console.WriteLine("Círculo:");
            Console.WriteLine("Área: " + circulo.CalcularArea());
            Console.WriteLine("Perímetro: " + circulo.CalcularPerimetro());

            // Crear un cuadrado con lado de 4 unidades
            Cuadrado cuadrado = new Cuadrado(4);
            Console.WriteLine("\nCuadrado:");
            Console.WriteLine("Área: " + cuadrado.CalcularArea());
            Console.WriteLine("Perímetro: " + cuadrado.CalcularPerimetro());
        }
    }
}
