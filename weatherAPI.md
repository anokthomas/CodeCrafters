https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={64aeae2f8ccb8eb3f197a7f24ad12c65}

const a = prompt("Please enter something:");
console.log("You entered:", a);        //Enter input ID in https format from front end

async function run() {

  const model = weatherAPI({ model: "weather-API 3.3"});

  const prompt = "From {"+a+",red,polyester},{Shirt,Yellow,cotton} choose a cloth to wear and give output in one word according to the climatic condition."

  const result = await model.generateContent(prompt);
  const response = await result.response;
  const text = response.text();
  console.log(text);
}

run();
