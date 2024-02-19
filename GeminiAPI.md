const { GoogleGenerativeAI } = require("@google/generative-ai");
const dotenv = require("dotenv")
dotenv.config()
// Initialize an empty array to store clothing items
const clothingArray = [];

// Prompt the user for the number of clothing items
const numberOfClothes = parseInt(prompt("How many clothing items do you want to add?"), 10);

// Validate if the input is a positive integer
if (isNaN(numberOfClothes) || numberOfClothes <= 0) {
  console.log("Please enter a valid positive integer for the number of clothing items.");
} else {
  // Loop through each clothing item
  for (let i = 0; i < numberOfClothes; i++) {
    const kindOfCloth = prompt(`Enter the kind of clothing #${i + 1}:`);
    const colorOfCloth = prompt(`Enter the color of clothing #${i + 1}:`);
    const materialOfCloth = prompt(`Enter the material of clothing #${i + 1}:`);

    // Create an object to represent the clothing item
    const clothingItem = {
      kind: kindOfCloth,
      color: colorOfCloth,
      material: materialOfCloth,
    };

    // Add the clothing item to the array
    clothingArray.push(clothingItem);
  }

  // Example usage:
  console.log("Added the following clothing items to the array:");
  console.log(clothingArray);
}

const genAI = new GoogleGenerativeAI(process.env.API_KEY);

async function run() {

  const model = genAI.getGenerativeModel({ model: "gemini-pro"});

  const prompt = "from Given the set of choices , give a one word answer for wearing with respect to current climatic conditions"

  const result = await model.generateContent(prompt);
  const response = await result.response;
  const text = response.text();
  console.log(text);
}
run();
