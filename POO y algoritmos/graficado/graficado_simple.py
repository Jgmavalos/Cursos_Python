from bokeh.plotting import figure, output_file, show

if __name__=='__main__':
    output_file('graficado_simple.html')
    fig = figure()
    # type() ver tipo de figura

    total_vals = int(input('Cuantos valores quieres graficar?: '))

    x_vals = list(range(total_vals))
    y_vals = []

    for i in x_vals:
        val = int(input(f'Valor Y para {i}: '))

    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)

    
