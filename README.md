# Negotiation Chatbot API

This project implements a chatbot that simulates price negotiation between a customer and a supplier, using AI (e.g., OpenAI GPT).

## Features

- User initiates price negotiation.
- Chatbot responds with either accepting the user's offer or proposing a counteroffer.
- AI-generated responses using OpenAI's GPT.
- Optional sentiment analysis: If the user is polite, the bot offers better deals.

## API Endpoints

### POST /negotiate

Send a JSON request with the user price and message for negotiation.

#### Request:
```json
{
  "user_input": "I'd like to get a discount, please!",
  "user_price": 75
}
