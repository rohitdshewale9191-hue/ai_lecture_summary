from gemini_client import get_client


client=get_client()

if client==None:
    print("Error")

else:
    interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="hi"
)
    print(interaction.output_text)
