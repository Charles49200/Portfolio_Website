function toggleMobileMenu(){
	document.getElementById("menu").classList.toggle("active");
}

const { OpenAIClient, AzureKeyCredential } = require("@azure/openai");
const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");

export async function main() {
    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
    const azureApiKey = process.env["AZURE_OPENAI_API_KEY"];
    const deploymentId = process.env["AZURE_OPENAI_DEPLOYMENT_ID"];
    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
    const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];

    if (!endpoint || !azureApiKey || !deploymentId || !searchEndpoint || !searchKey || !searchIndex) {
        console.error("Please set the required environment variables.");
        return;
    }

    const client = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));

    const messages = [
        { role: "system", content: "You are an AI assistant that helps people to understand Tarzan's cv letter." },
        { role: "user", content: "" }
    ];
    console.log(`Message: ${messages.map((m) => m.content).join("\n")}`);

    const events = await client.streamChatCompletions(deploymentId, messages, {
        pastMessages: 10,
        maxTokens: 800,
        temperature: 0,
        topP: 1,
        frequencyPenalty: 0,
        presencePenalty: 0,
        azureExtensionOptions: {
            extensions: [
                {
                    type: "AzureCognitiveSearch",
                    endpoint: searchEndpoint,
                    key: searchKey,
                    indexName: searchIndex,
                },
            ],
        },
    });

    let response = "";
    for await (const event of events) {
        for (const choice of event.choices) {
            const newText = choice.delta?.content;
            if (!!newText) {
                response += newText;
                // To see streaming results as they arrive, uncomment line below
                // console.log(newText);
            }
        }
    }
    console.log(response);
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});


document.getElementById('contactForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value,
    };

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    try {
        const response = await fetch('http://localhost:8000/api/contact-form/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            alert('Form submitted successfully');
            document.getElementById('contactForm').reset();
        } else {
            alert('Form submission failed');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error submitting the form');
    }
});
