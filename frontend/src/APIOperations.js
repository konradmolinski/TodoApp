const { VITE_API_URL } = import.meta.env;

const URL_TASKS = `${VITE_API_URL}todos`;

function handleErrors(response) {
  if (!response.ok) {
    if (response.status === 401) {
      window.Cookie.clear('secret').then();
      location.reload(); // eslint-disable-line
    }
    // eslint-disable-next-line no-alert
    alert(response.statusText);
  }
  return response;
}

export function getTasks() {
  return fetch(URL_TASKS, { method: 'GET', credentials: 'include' })
    .then(handleErrors)
    .then((response) => response.json())
    .then((json) => json);
}

export function setTaskCompleted(taskId) {
  return fetch(URL_TASKS, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ task_id: taskId }),
  })
    .then(handleErrors);
}
