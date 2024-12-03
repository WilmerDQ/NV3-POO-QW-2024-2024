using System;

namespace FigurasGeometricas
{
    // Clase para representar un círculo
    public class Circulo
    {
        // Propiedad para almacenar el radio del círculo
        public double Radio { get; set; }

        // Constructor para inicializar el radio
        public Circulo(double radio)
        {
            Radio = radio;
        }

        // Método para calcular el área del círculo
        // Fórmula: área = π * radio^2
        public double CalcularArea()
        {
            return Math.PI * Math.Pow(Radio, 2);
        }

        // Método para calcular el perímetro del círculo
        // Fórmula: perímetro = 2 * π * radio
        public double CalcularPerimetro()
        {
            return 2 * Math.PI * Radio;
        }
    }
}
