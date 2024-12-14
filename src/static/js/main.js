function waitForDocument(attempt, retries) {
  setTimeout(function() {
    fetch("/document_readiness").then(function(response) {
      if (!response.ok) {
         throw new Error(`HTTP error! status: ${response.status}`);
      }

      const responseJson = response.json();
      console.log("resp", responseJson);
    });

    if (attempt < retries) {
      console.log("retrying...", attempt)
      waitForDocument(attempt+1, retries);
    } else {
      console.log("Max attempts reached")
    }
  }, 1000);

}

if (context.pending_document) {
  waitForDocument(0, 10)
}
