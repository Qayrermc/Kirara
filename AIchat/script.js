import { GenerativeLanguageClient } from "@google-ai/generativelanguage";

const apiKey = "AIzaSyClZePx68pVE3oEooacQ93UljzBzVlW3s0"; // Thay bằng API key của bạn

const client = new GenerativeLanguageClient({
  apiKey: apiKey,
});

async function hoiGemini(cauHoi) {
  const response = await client.generateText({
    model: "gemini-1.5-flash-latest",
    prompt: cauHoi,
  });
  return response.candidates[0].output;
}

// Lấy các phần tử HTML
const input = document.getElementById("input");
const output = document.getElementById("output");
const button = document.getElementById("button");

// Thêm event listener cho nút
button.addEventListener("click", () => {
  const cauHoi = input.value;
  hoiGemini(cauHoi)
    .then((traLoi) => {
      output.textContent = traLoi;
    })
    .catch((error) => {
      console.error("Lỗi:", error);
      output.textContent = "Đã xảy ra lỗi.";
    });
});