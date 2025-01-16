# Value at Risk (VaR) Calculator

## Description

This project calculates the **Value at Risk (VaR)** of a financial portfolio using a parametric method based on the simulated returns normal distribution. VaR is a risk management tool that estimates the maximum potential loss of a portfolio at a certain confidence level over a given time period. This project is designed to demonstrate a simple and parametric approach to calculating VaR.

VaR is widely used in finance to measure the risk of loss in a portfolio. In this project, we calculate the VaR based on simulated returns, and the confidence level can be adjusted as needed.

## Features

- Generation of **simulated returns** based on a normal distribution (with specified mean and standard deviation).
- Calculation of **parametric VaR** at a specified confidence level.
- Visualization of the simulated returns as a histogram, with a line indicating the VaR.

## Installation

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/TKoskas/VaR-Calculation.git
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```
The required libraries are:
- `numpy`
- `pandas`
- `matplotlib`
## Usage
1.	Run the Python script to generate the simulated returns and calculate the VaR:
```bash
python var_calculator.py
```
2.	The VaR will be calculated for a default confidence level of 95%. You can adjust the confidence level by modifying the confidence_level variable in the script.
3.	The generated plot will display the simulated returns as a histogram, with a red line representing the VaR.
## Example Output
```bash
VaR at 95.0% confidence level: -0.0148
```
The generated graph will show the distribution of the simulated returns, with a vertical line marking the VaR value.

Authors : 
**Thomas Koskas**
## License
This project is licensed under the MIT License
