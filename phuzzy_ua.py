# phuzzy_ua.py
# sample page response

def lambda_handler(event, context):
  print("Event triggered")
  html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
  </head>
  <body>
    <h1>Success!</h1>
    <p>The action was completed successfully.</p>
  </body>
</html>
"""
  # Construct the response
  response = {
      'statusCode': 200,
      'headers': {
          'Content-Type': 'text/html'
      },
      'body': html_content
  }
  
  return response
  # comment to test deployment
