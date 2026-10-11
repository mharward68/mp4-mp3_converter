import type { Config, Context } from "@netlify/functions";
import { getStore } from "@netlify/blobs";

// Anonymous usage tally. Each call writes one tiny record named
// "<event>/<YYYY-MM-DD>/<random id>". Nothing about the visitor or their files is stored.
// One record per event (no shared counter) so simultaneous calls can never overwrite each other.
const EVENTS = new Set(["visit", "install", "convert"]);

export default async (req: Request, _context: Context) => {
  const event = new URL(req.url).searchParams.get("e") ?? "";
  if (!EVENTS.has(event)) return new Response(null, { status: 400 });
  const day = new Date().toISOString().slice(0, 10);
  await getStore("usage").set(`${event}/${day}/${crypto.randomUUID()}`, "1");
  return new Response(null, { status: 204 });
};

export const config: Config = {
  path: "/api/count",
  method: ["POST"],
  rateLimit: { action: "rate_limit", aggregateBy: ["ip", "domain"], windowSize: 60, windowLimit: 60 },
};
