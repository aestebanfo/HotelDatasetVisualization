import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import base64

# Initialize Dash app
app = dash.Dash(__name__)

# Paths to images (ensure these images are correct paths to your PNG files)
graph_1_1_path = './images/graph_1_1.png'
graph_1_2_path = './images/graph_1_2.png'
graph_2_1_path = './images/graph_2_1.png'
graph_2_2_path = './images/graph_2_2.png'
graph_3_1_path = './images/graph_3_1.png'
graph_3_2_path = './images/graph_3_2.png'
worker_image_path = './images/worker.png'  # Ensure correct path
worker_1_1_path = './images/worker_1_1.png'
worker_1_2_path = './images/worker_1_2.png'
worker_2_1_path = './images/worker_2_1.png'
worker_2_2_path = './images/worker_2_2.png'
worker_3_1_path = './images/worker_3_1.png'
worker_3_2_path = './images/worker_3_2.png'
bg2_path = './images/bg1.jpeg'  # Resort background
bg1_path = './images/bg2_cropped_top.jpeg'  # Updated to cropped top

# Function to encode images to base64
def encode_image(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Encode all images into base64
encoded_worker_image = encode_image(worker_image_path)
encoded_worker_1_1 = encode_image(worker_1_1_path)
encoded_worker_1_2 = encode_image(worker_1_2_path)
encoded_worker_2_1 = encode_image(worker_2_1_path)
encoded_worker_2_2 = encode_image(worker_2_2_path)
encoded_worker_3_1 = encode_image(worker_3_1_path)
encoded_worker_3_2 = encode_image(worker_3_2_path)
encoded_graph_1_1 = encode_image(graph_1_1_path)
encoded_graph_1_2 = encode_image(graph_1_2_path)
encoded_graph_2_1 = encode_image(graph_2_1_path)
encoded_graph_2_2 = encode_image(graph_2_2_path)
encoded_graph_3_1 = encode_image(graph_3_1_path)
encoded_graph_3_2 = encode_image(graph_3_2_path)
encoded_bg1 = encode_image(bg1_path)
encoded_bg2 = encode_image(bg2_path)

# Layout of the app
app.layout = html.Div([
    html.H1('Portuguese Hotel Worker Accomodation to Foreigners', style={'text-align': 'center'}),  # Centered title
    
    # Image container for the current stage (this will be overwritten)
    html.Div(id='image-container', children=[
        html.Img(src=f"data:image/jpeg;base64,{encoded_worker_image}", id='worker-image', style={'width': '150px', 'height': 'auto'})
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '80vh'}),  # Center worker image in the viewport

    # "Next" button to trigger the change
    html.Button('Next', id='next-button', n_clicks=0, style={
        'position': 'absolute', 'bottom': '20px', 'right': '40px', 'padding': '10px 20px', 'font-size': '16px'
    }),

    # "Before" button to go back (optional, if you want to go back in the sequence)
    html.Button('Before', id='before-button', n_clicks=0, style={
        'position': 'absolute', 'bottom': '20px', 'left': '40px', 'padding': '10px 20px', 'font-size': '16px'
    }),

    # Text below the images
    html.Div(id='explanation-text', style={'text-align': 'center', 'padding': '20px'})
], style={'position': 'relative', 'min-height': '100vh'})  # Ensure the page takes up at least the full viewport height

# Callback to update the layout when the "Next" or "Before" button is clicked


text_div_2 = html.Div([
    # Storytelling Section
    html.Div([
        html.P("Meet Our Workers: Twin Brothers, a Passion for Data and Adapting to New Challenges", style={'font-weight': 'bold', 'font-size': '20px'}),

        # Left Worker (João - City Hotel)
        html.Div([
            html.Div([
                html.P("Meet João Silva and his twin brother Pedro Silva. Born and raised in Portugal, these two brothers share a deep passion for data and a drive to understand customer behavior. Growing up in a family that worked in hospitality, both João and Pedro were inspired to pursue careers in the hotel industry. João chose to work in a bustling city hotel in Lisbon, while Pedro took a position at a resort hotel in the Algarve.", style={'text-align': 'justify'}),
                html.P("As João settled into his role at the city hotel, he began noticing a growing trend: more and more international guests were booking stays, bringing with them different preferences and expectations. João, familiar with the local Portuguese guests, realized that foreign visitors had distinct behaviors and needs. This realization prompted João to dive deeper into the hotel booking data to understand what factors were influencing these foreign clients' decisions, and how he could better adapt the city hotel’s services to meet their expectations.", style={'text-align': 'justify'}),
                html.P("Determined to cater to this new type of clientele, João started analyzing booking patterns, spending behaviors, and booking lead times. He wanted to ensure that his hotel could stand out to foreign visitors and offer them a personalized experience that would make them feel at home in the city.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'}),

        # Right Worker (Pedro - Resort Hotel)
        html.Div([
            html.Div([
                html.P("Pedro Silva, João's twin brother, works at a resort hotel in the Algarve. Like João, Pedro always had a keen interest in data and customer behavior. After joining the resort, Pedro quickly realized that the influx of foreign guests brought new challenges. The resort’s international visitors had distinct preferences, such as the type of activities they enjoyed, the amenities they sought, and how long they stayed.", style={'text-align': 'justify'}),
                html.P("Pedro, much like his brother, recognized that the resort needed to adapt its services to better cater to this growing segment of international guests. He turned to the hotel booking dataset to understand guest behaviors, focusing on metrics like booking frequency, guest nationality, and average spending per guest. Pedro's goal was to personalize the resort’s offerings, from activities to room selection, ensuring that foreign visitors had the best possible experience during their stay.", style={'text-align': 'justify'}),
                html.P("By using data insights, Pedro hoped to make the resort a favorite destination for international guests, ultimately increasing repeat bookings and enhancing the resort’s reputation for excellent service and tailored guest experiences.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding': '20px'})
])


text_div_3 = html.Div([
    # Findings and Analysis Section
    html.Div([
        html.P("Findings: Most Frequent Visitors by Country", style={'font-weight': 'bold', 'font-size': '20px'}),

        # City Hotel Findings
        html.Div([
            html.Div([
                html.P("Through the analysis of booking data, we observed the most frequent visitors to the City Hotel in Lisbon. The top countries based on booking frequency were the United Kingdom (UK) and Spain. These two countries consistently showed high booking numbers, with the UK leading the way, followed closely by Spain.", style={'text-align': 'justify'}),
                html.P("The presence of a large number of visitors from the UK and Spain could be attributed to geographical proximity, cultural similarities, and strong economic ties between Portugal and these nations. Additionally, both countries are well-connected to Portugal through direct flights, making it an easy and convenient destination for both leisure and business travel.", style={'text-align': 'justify'}),
                html.P("For the City Hotel, this trend has significant implications for business strategy. Hotels may want to tailor their marketing efforts to emphasize offers that appeal specifically to these nationalities, such as promotions highlighting local culture and events popular among British and Spanish tourists. Additionally, providing multilingual staff and offering services that cater to their cultural preferences (e.g., food, entertainment) can help improve guest satisfaction and loyalty.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'}),

        # Resort Hotel Findings
        html.Div([
            html.Div([
                html.P("On the other hand, the Resort Hotel in the Algarve saw the highest number of bookings from France and Germany. These countries showed the strongest interest in visiting the resort, with France leading the charge and Germany following closely behind.", style={'text-align': 'justify'}),
                html.P("The popularity of France and Germany as key sources of international bookings for the Resort Hotel could be due to several factors, including the high demand for luxury resorts among French and German tourists, as well as the Algarve's reputation as a premium vacation destination. Both France and Germany also have a large number of affluent travelers seeking leisure experiences that combine relaxation and cultural exploration.", style={'text-align': 'justify'}),
                html.P("For the Resort Hotel, this insight can have a significant impact on future business strategies. Hotels may consider developing targeted marketing campaigns focusing on French and German travelers, offering tailored packages for relaxation, family holidays, and cultural experiences. Additionally, collaborating with local travel agencies in these countries to create special vacation packages could help attract more visitors from these regions. Offering German- and French-speaking staff and providing region-specific amenities could also enhance guest satisfaction and increase repeat bookings.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding': '20px'})
])


text_div_4 = html.Div([
    # Explanation of their Appearance Change
    html.Div([
        html.P("Adapting to Their New Roles: A Symbolic Change in Appearance", style={'font-weight': 'bold', 'font-size': '20px'}),

        # City Hotel Worker (João) - Bowler Hat
        html.Div([
            html.Div([
                html.P("Having understood the key markets for their respective hotels, João decided to make a symbolic change in his appearance to better reflect his new focus on attracting UK and Spanish guests. As the City Hotel in Lisbon saw the highest number of bookings from the United Kingdom and Spain, João thought it fitting to adopt a traditional British accessory: the bowler hat. This subtle change in his attire represents his commitment to welcoming British guests with familiarity and a sense of cultural connection.", style={'text-align': 'justify'}),
                html.P("The bowler hat, a staple of British fashion, symbolizes João's understanding of the cultural nuances that make British guests feel at ease. Whether it’s the food offerings, the style of service, or the overall ambiance of the hotel, João’s decision to don the bowler hat is a fun, yet meaningful way of signaling that the City Hotel is ready to cater to the unique needs of its British and Spanish clientele.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'}),

        # Resort Hotel Worker (Pedro) - Beret
        html.Div([
            html.Div([
                html.P("On the other hand, Pedro, working at the Resort Hotel in the Algarve, noticed that French and German visitors were the primary clientele. To symbolically align with his focus on these countries, Pedro chose to wear a beret, a classic French accessory that signifies a welcoming and cultural connection with French tourists. The beret also subtly acknowledges the German influence, given the shared European cultural context.", style={'text-align': 'justify'}),
                html.P("Pedro’s beret represents his commitment to making French and German visitors feel at home at the resort. The resort’s offerings, from language options to leisure activities, have been tailored to cater specifically to the tastes and preferences of these guests. By wearing the beret, Pedro signals his dedication to creating a personalized and culturally resonant experience for his French and German clientele.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding': '20px'})
])
text_div_5 = html.Div([
    # Findings and Explanation on Top Countries by Average ADR
    html.Div([
        html.P("Top Countries by Average ADR: Rare but High-Spending Guests", style={'font-weight': 'bold', 'font-size': '20px'}),

        # City Hotel Findings
        html.Div([
            html.Div([
                html.P("In the City Hotel in Lisbon, the countries with the highest Average Daily Rate (ADR) were Anguilla, Comoros, and United States Minor Outlying Islands. While these countries had only one booking each, resulting in disproportionately high ADRs, it's important to note that these guests were extremely high spenders.", style={'text-align': 'justify'}),
                html.P("Despite the low number of bookings from these countries, João recognizes that these rare guests bring in significant revenue per stay. The single booking from each country might have been a premium reservation, contributing to the unusually high ADR. This insight is crucial, as these guests, although rare, are not only valuable but represent a lucrative opportunity for the City Hotel.", style={'text-align': 'justify'}),
                html.P("Understanding that these guests might be high-value but infrequent, João has made it a priority to ensure they receive the best possible service. He has implemented strategies to accommodate these special guests with tailored, VIP-level treatment. Whether it's personalized services, luxury packages, or exclusive experiences, João ensures that every rare guest is treated like royalty, making their stay unforgettable and potentially encouraging repeat visits.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'}),

        # Resort Hotel Findings
        html.Div([
            html.Div([
                html.P("Similarly, at the Resort Hotel in the Algarve, Senegal, Djibouti, and Andorra appeared as top countries by ADR. Although these countries had only one booking each, leading to high ADR values, Pedro recognizes that these rare visitors are likely to be high spenders. A single booking from these countries likely involved a premium stay, such as a luxury suite or extended vacation.", style={'text-align': 'justify'}),
                html.P("While these countries do not represent a large volume of guests, their high spending per booking makes them significant. Pedro understands the importance of providing special attention to these rare but lucrative guests, ensuring they feel valued and have an extraordinary experience during their stay.", style={'text-align': 'justify'}),
                html.P("Pedro’s approach is to go beyond standard services for these high-spending visitors. The Resort Hotel is now ready to provide tailored experiences, exclusive packages, and personalized services to cater to these guests’ needs. By offering VIP treatment and premium services, Pedro is ensuring that these rare but valuable guests leave with a lasting positive impression and a desire to return.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding': '20px'})
])

text_div_6= html.Div([
    # New Page / New Section
    html.Div([
        html.P("Adapting to Rare, High-Spending Guests: João and Pedro's Commitment", style={'font-weight': 'bold', 'font-size': '20px', 'text-align': 'center'}),
        
        # Shortened Content
        html.Div([
            html.P("João at the City Hotel noticed rare but high-spending guests from countries like Anguilla. Although bookings from these countries were few, they brought significant revenue. To show his commitment, João proudly holds a flag of Anguilla, ensuring these guests feel valued despite their rarity.", style={'text-align': 'justify'}),
            html.P("At the Resort Hotel, Pedro faces a similar situation with rare visitors from Senegal and other countries. To symbolize his respect, Pedro wears a dashiki from Senegal, reflecting his dedication to offering special attention to these high-spending, unique guests.", style={'text-align': 'justify'}),
            html.P("Both João and Pedro know that these rare but valuable guests deserve personalized service and will go the extra mile to make them feel at home.", style={'text-align': 'justify'}),
        ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),
    ], style={'padding': '20px'})
])

text_div_7 = html.Div([
    # Explanation of Repeated Guest Focus
    html.Div([
        html.P("Focusing on Repeat Guests: João and Pedro’s Personalized Approach", style={'font-weight': 'bold', 'font-size': '20px'}),

        # City Hotel Worker (João) - Focus on France and Spain
        html.Div([
            html.Div([
                html.P("At the City Hotel, João recognized that the highest number of repeated guests came from France and Spain. With this insight, João decided to focus more on these loyal customers and enhance their experience. He is committed to making these returning guests feel welcomed and valued. By tailoring the services to their preferences, João ensures that these guests continue to choose the City Hotel as their preferred destination.", style={'text-align': 'justify'}),
                html.P("João is focused on building stronger relationships with guests from these countries. Whether it's by offering personalized services, providing language support, or introducing special packages, João’s dedication to repeat visitors is clear. His goal is to ensure that every return guest feels like part of the City Hotel family.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'}),

        # Resort Hotel Worker (Pedro) - Focus on United Kingdom
        html.Div([
            html.Div([
                html.P("Meanwhile, Pedro at the Resort Hotel in the Algarve noticed that the United Kingdom dominated the list of repeat visitors. This insight led Pedro to focus even more on this key market. He aims to create an exceptional experience for British guests, ensuring they return time and again. Pedro believes that understanding the preferences of this loyal market will help the resort deliver the best possible experience to these repeat guests.", style={'text-align': 'justify'}),
                html.P("Pedro is adapting the resort’s offerings to appeal specifically to UK visitors. From customized activities to exclusive packages, Pedro is making sure the Resort Hotel remains the top choice for British tourists looking for a relaxing vacation. His efforts show his commitment to making the UK guests feel at home and appreciated every time they return.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding': '20px'})
])

text_div_8= html.Div([
    # Final Reflection on Learning and Data Usage
    html.Div([
        html.P("Learning from Data: João and Pedro’s Path to Better Accommodation", style={'font-weight': 'bold', 'font-size': '20px'}),

        # City Hotel Worker (João) - How Data Helps João
        html.Div([
            html.Div([
                html.P("João’s experience at the City Hotel has shown him the power of data in identifying key markets, like France and Spain, for repeat guests. By analyzing booking patterns and customer behavior, João has learned how to adapt the hotel’s offerings to meet the specific needs of these loyal visitors. With data-driven insights, João now tailors the hotel’s services, from language preferences to cultural nuances, ensuring each guest feels at home.", style={'text-align': 'justify'}),
                html.P("João understands that the key to improving the hotel’s success lies in personalizing the experience for his repeat guests. By constantly analyzing customer feedback, booking frequencies, and even special requests, João can adjust the hotel’s approach, leading to increased guest satisfaction and higher chances of return bookings.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'}),

        # Resort Hotel Worker (Pedro) - How Data Helps Pedro
        html.Div([
            html.Div([
                html.P("Pedro’s time at the Resort Hotel has reinforced the importance of data in identifying patterns, especially when it comes to repeat visitors from the United Kingdom. Through analyzing booking history and guest preferences, Pedro has gained valuable insights into what makes these guests return time and time again. By focusing on this data, Pedro can create tailored experiences that cater to their specific needs and desires.", style={'text-align': 'justify'}),
                html.P("For Pedro, the power of data lies in its ability to highlight what’s working and what needs improvement. With detailed insights into customer behavior, he’s able to refine the resort’s offerings, introduce new services, and implement strategies that specifically appeal to the UK market. This not only boosts customer satisfaction but also enhances the likelihood of long-term repeat business.", style={'text-align': 'justify'})
            ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center'}),

        ], style={'display': 'inline-block', 'width': '48%', 'vertical-align': 'top', 'padding': '10px'}),

        # Shared Conclusion: Power of Data
        html.Div([
            html.P("Both João and Pedro have come to realize that data is a powerful tool in driving better business outcomes. By understanding customer preferences, booking trends, and guest behaviors, they can create more personalized experiences that cater to the specific needs of international and repeat guests. This targeted approach not only enhances the guest experience but also ensures that both hotels remain competitive and successful in a dynamic hospitality market.", style={'text-align': 'justify'})
        ], style={'max-width': '800px', 'margin': '0 auto', 'text-align': 'center', 'padding': '10px'})
    ], style={'padding': '20px'})
])

@app.callback(
    [Output('image-container', 'children'),
     Output('explanation-text', 'children')],
    [Input('next-button', 'n_clicks'),Input('before-button', 'n_clicks')]
)
def update_images(next_clicks,before_clicks):
    n_clicks=next_clicks%8-before_clicks%8
    if n_clicks == 0:
        # Display just the worker image

        text_div= html.Div([
        html.Div([
            html.P("Introduction to the Hotel Booking Demand Dataset", style={'font-weight': 'bold', 'font-size': '20px'}),
            html.P("The Hotel Booking Demand Dataset is a comprehensive collection of data related to hotel bookings, primarily in Portugal. It offers a detailed view of the factors influencing hotel demand, allowing for deeper insights into booking patterns, customer preferences, and industry trends. The dataset includes various attributes that capture the complexities of hotel management and customer behavior, such as booking dates, customer demographics, and booking status. This data can be used to analyze key trends like booking lead times, cancellation rates, and stay durations, all of which are vital for hotel staff and managers in optimizing operations and enhancing guest experiences."),
            html.P("Data Overview:"),
            html.Ul([
                html.Li("Hotel Type: City or Resort hotel"),
                html.Li("Booking Date and Lead Time: The number of days between when a booking was made and the guest’s arrival date"),
                html.Li("Stay Duration: The length of the guest’s stay"),
                html.Li("Booking Status: Whether the booking was canceled or confirmed"),
                html.Li("Customer Segments: The market channel through which the booking was made (e.g., online, corporate)"),
                html.Li("Customer Demographics: Information like the country of origin and special requests made by guests"),
                html.Li("Booking Source: The channel through which the booking was made (e.g., direct, travel agency)"),
                html.Li("Number of Guests: Total number of adults and children in the booking"),
            ]),
            html.P("This dataset provides a valuable snapshot of hotel demand trends in Portugal and can be used for various analyses related to customer segmentation, demand forecasting, resource planning, and operational management."),
        ], style={'textAlign': 'center', 'max-width': '800px', 'margin': '0 auto'}),

    # Analysis text
    html.Div([
        html.Div([
            html.P("Focus of Our Analysis: Non-Portuguese Clients and Targeted Accommodation Strategies", style={'font-weight': 'bold', 'font-size': '20px'}),
            html.P("In our analysis, we’ve specifically focused on non-Portuguese clients to identify patterns and insights that can help hotels optimize their accommodation strategies for international guests. By isolating these non-Portuguese bookings, we aim to determine which countries generate the highest demand for hotel stays in Portugal, allowing hotel managers to tailor their efforts toward attracting guests from specific regions."),
            html.P("We’ve also divided the data into two categories: City Hotels and Resort Hotels, to analyze if there are notable differences in how guests from different countries prefer to book or stay in each type of accommodation."),
            html.P("Our main objective is to understand:"),
            html.Ul([
                html.Li("Which are the most frequent visitors to city vs. resort hotels?"),
                html.Li("Which are the ones that spend the most at each type of accommodation?"),
                html.Li("Which are the visitors who repeat their stays more frequently?"),
            ]),
            html.P("By analyzing these factors, we can identify key markets where hotels might want to focus their marketing efforts, adjust pricing strategies, or enhance specific services to better cater to international guests. This targeted approach will help optimize hotel resources and improve guest satisfaction by focusing on the most promising international markets."),
        ], style={'textAlign': 'center', 'max-width': '800px', 'margin': '0 auto'}),
    ])])



        
        return html.Div([
            html.Img(src=f"data:image/jpeg;base64,{encoded_worker_image}", id='worker-image', style={'width': '300px', 'height': 'auto'})
        ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '80vh'}), text_div
    
    elif n_clicks == 1 or n_clicks == 3 or n_clicks==5 or n_clicks == 7:
        worker_image_1 = encoded_worker_image
        worker_image_2 = encoded_worker_image
        text_div=text_div_2
        if n_clicks == 3:
            worker_image_1 = encoded_worker_1_1
            worker_image_2 = encoded_worker_1_2
            text_div=text_div_4
            
        elif n_clicks==5:
            worker_image_1 = encoded_worker_2_1
            worker_image_2 = encoded_worker_2_2
            text_div=text_div_6
        elif n_clicks == 7:
            worker_image_1 = encoded_worker_3_1
            worker_image_2 = encoded_worker_3_2
            text_div=text_div_8
        return html.Div([
            html.Div([
                html.Img(src=f"data:image/jpeg;base64,{encoded_bg1}", style={'width': '800px', 'height': 'auto', 'display': 'inline-block'}),
                html.Img(src=f"data:image/jpeg;base64,{worker_image_1}", style={'width': '300px', 'height': 'auto', 'position': 'absolute', 'top': '40%', 'left': '50%', 'transform': 'translateX(-50%)'})
            ], style={'position': 'relative', 'display': 'inline-block'}),
            html.Div([
                html.Img(src=f"data:image/jpeg;base64,{encoded_bg2}", style={'width': '800px', 'height': 'auto', 'display': 'inline-block'}),
                html.Img(src=f"data:image/jpeg;base64,{worker_image_2}", style={'width': '300px', 'height': 'auto', 'position': 'absolute', 'top': '40%', 'left': '50%', 'transform': 'translateX(-50%)'})
            ], style={'position': 'relative', 'display': 'inline-block'})
        ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '80vh'}), text_div
    
    elif n_clicks == 2 or n_clicks==4 or n_clicks==6:
        text_div=''
        if n_clicks == 2:
            text_div=text_div_3
            encoded_graph_1 = encoded_graph_1_1
            encoded_graph_2 = encoded_graph_1_2
        elif n_clicks==4:
            encoded_graph_1 = encoded_graph_2_1
            encoded_graph_2 = encoded_graph_2_2
            text_div=text_div_5
        elif n_clicks == 6:
            encoded_graph_1 = encoded_graph_3_1
            encoded_graph_2 = encoded_graph_3_2
            text_div=text_div_7
        # Show graph_1_1 and graph_1_2 with explanation
        return html.Div([
            html.Div([
                html.Img(src=f"data:image/png;base64,{encoded_graph_1}", style={'width': '800px', 'height': 'auto'}),
                html.Img(src=f"data:image/png;base64,{encoded_graph_2}", style={'width': '800px', 'height': 'auto'})
            ], style={'display': 'flex', 'justify-content': 'space-around', 'align-items': 'center'}),
        ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '80vh'}), text_div
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)