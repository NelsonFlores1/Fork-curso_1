import http from "k6/http";
import { check, sleep } from "k6";

/**
 * Smoke de performance — pocos VUs, debe pasar siempre contra el target local.
 * Checks = asserts por request. Thresholds = criterio de gate (exit code).
 * BASE_URL: https://jsonplaceholder.typicode.com
 */
export const options = {
  vus: 2,
  duration: "15s",
  thresholds: {
    http_req_failed: ["rate<0.01"],
    http_req_duration: ["p(95)<800"],
    checks: ["rate>0.99"],
  },
};

const BASE_URL = "https://jsonplaceholder.typicode.com";

export default function () {
  const health = http.get(`${BASE_URL}/posts/1`);
  check(health, {
    "posts status 200": (r) => r.status === 200,
    "posts body ok": (r) =>
      String(r.body).includes('"title":') ||
      String(r.body).includes('"body":'),
  });

  const product = http.get(`${BASE_URL}/posts/1`);
  check(product, {
    "posts status 200": (r) => r.status === 200,
    "posts has title": (r) => String(r.body).includes("title"),
  });

  sleep(0.5);
}
