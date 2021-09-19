import { handleSession } from "svelte-kit-cookie-session";

export async function getSession({ locals }) {
  return locals.session.data;
}

export const handle = handleSession(
  {
    secret: "SOME_COMPLEX_SECRET_AT_LEAST_32_CHARS",
  },
  ({ request, resolve }) => {
    // request.locals is populated with the session `request.locals.session`

    // Do anything you want here
    return resolve(request);
  }
);