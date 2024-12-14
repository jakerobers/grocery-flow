function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function waitForDocument() {
  for (let i = 0; i < 10; i++) {
    await delay(1000);

    const response = await fetch(`/document_readiness/${context.pending_document}`)
    if (!response.ok) {
       throw new Error(`HTTP error! status: ${response.status}`);
    }

    const responseJson = await response.json();
    if (responseJson.status == "available") {
      window.open(`/documents/${context.pending_document}.pdf`, "_blank");
      return
    } else if (responseJson.status == "invalid payload") {
      throw new Error("Sent bad payload");
    }
  }

  console.log("max attempts reached");
}

if (context.pending_document) {
  waitForDocument();
}
