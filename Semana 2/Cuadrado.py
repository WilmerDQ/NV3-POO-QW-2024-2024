using System;

namespace FigurasGeometricas
{
    // Clase para representar un cuadrado
    public class Cuadrado
    {
        // Propiedad para almacenar el lado del cuadrado
        public double Lado { get; set; }

        // Constructor para inicializar el lado
        public Cuadrado(double lado)
        {
            Lado = lado;
        }

        // Método para calcular el área del cuadrado
        // Fórmula: área = lado^2
        public double CalcularArea()
        {
            return Math.Pow(Lado, 2);
        }

        // Método para calcular el perímetro del cuadrado
        // Fórmula: perímetro = 4 * lado
        public double CalcularPerimetro()
        {
            return 4 * Lado;
        }
    }
}
