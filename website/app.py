import dash
from dash import html, dcc, Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# List of image URLs or paths
image_list = ["/assets/images/" + str(x).zfill(7) + '.png' for x in range(60,5160,60)]
#image_list = ['/assets/0000100.png']

app.layout = html.Div([
    dcc.Slider(
        id='image-slider',
        min=0,
        max=len(image_list) - 1,
        value=0,
        step=1,
        marks={i: '{}'.format(i + 1) for i in range(len(image_list))},
    ),
    html.Div(id='slider-output-container'),
    html.Img(id='image-display', src=image_list[0], style={'width': '100%', 'height': 'auto'})
])


@app.callback(
    Output('image-display', 'src'),
    Input('image-slider', 'drag_value'))
def update_image(selected_image_index):
    if(selected_image_index is None):
        selected_image_index = 0
    return image_list[selected_image_index]

if __name__ == '__main__':
    app.run_server(debug=True, host='192.168.208.73')
