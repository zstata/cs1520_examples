function setup() {
	poller();
}

function poller() {
	console.log("Polling for new Todos");
	fetch("/todos")
		.then((response) => {
			return response.json();
		})
		.then((response) => {
			console.log(`Got this response: ${response}`);
			// Should repopulate the list
		})
		.catch((err) => {
			console.log(`Error polling for new todos: ${err}`);
		});
}

// TODO:
// Write DOM manipulation function to repopulate the list
// Call timeout to recall poller() after a set time period
// Write fetch() to delete a todo item
// Write fetch() to mark a todo item done
// Write fetch() to post a new todo item 

window.addEventListener("load", setup);
