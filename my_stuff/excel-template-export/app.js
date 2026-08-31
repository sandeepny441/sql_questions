const defaultTopics = [
  {
    name: "Mercury",
    cards: [
      {
        letter: "a",
        abbreviation: "ORB",
        term: "Orbital Year",
        definition: "Mercury circles the Sun in just 88 Earth days.",
        explanation:
          "Its year is short because it travels close to the Sun on a tight, fast path.",
        story:
          "I imagine celebrating my birthday on Mercury and blowing out candles four times before one Earth year is over. That makes the planet feel less like a distant dot and more like a place where the calendar rushes ahead of me.",
      },
      {
        letter: "b",
        abbreviation: "TEMP",
        term: "Temperature Swing",
        definition: "Mercury swings from blazing hot in sunlight to freezing cold in darkness.",
        explanation:
          "With almost no real atmosphere to trap heat, the surface cannot hold a steady temperature.",
        story:
          "I picture standing on one side of Mercury feeling like my shoes are on a grill, then stepping into shadow and suddenly wanting the thickest winter coat I own. That wild flip helps me understand why Mercury is a planet of extremes.",
      },
      {
        letter: "c",
        abbreviation: "CORE",
        term: "Iron Core",
        definition: "Mercury has an unusually large iron core for such a small planet.",
        explanation:
          "That metal-heavy center helps Mercury keep a magnetic field even though the planet itself is tiny.",
        story:
          "I think of Mercury as a small fruit with a giant pit in the middle. Once I picture that oversized iron center, the planet stops feeling ordinary and starts feeling like a compact metal world wearing a thin rocky shell.",
      },
      {
        letter: "d",
        abbreviation: "SKY",
        term: "Thin Exosphere",
        definition: "Mercury has only a whisper-thin exosphere instead of a full atmosphere.",
        explanation:
          "Its gases are so sparse that the sky would not behave anything like Earth's air.",
        story:
          "If I could stand there, I would not feel wind on my face or see clouds rolling by. I would feel like I was on a bare stage with space pressing in from every direction.",
      },
    ],
  },
  {
    name: "Venus",
    cards: [
      {
        letter: "a",
        abbreviation: "HEAT",
        term: "Extreme Heat",
        definition: "Venus is the hottest planet in the solar system.",
        explanation:
          "Its thick atmosphere traps heat so effectively that even Mercury is cooler overall.",
        story:
          "I imagine opening an oven and then realizing Venus would still make that heat feel mild. That comparison helps me feel just how brutally hot the planet really is.",
      },
      {
        letter: "b",
        abbreviation: "DAY",
        term: "Slow Day",
        definition: "One day on Venus lasts longer than one year on Venus.",
        explanation:
          "The planet spins so slowly that a full turn takes more time than its trip around the Sun.",
        story:
          "I picture waking up on Venus and waiting so long for tomorrow that the whole planet finishes another lap around the Sun first. That makes its slow spin feel wonderfully strange instead of just technical.",
      },
      {
        letter: "c",
        abbreviation: "AIR",
        term: "Carbon Dioxide Air",
        definition: "Venus has a very thick atmosphere made mostly of carbon dioxide.",
        explanation:
          "That heavy blanket of gas is one big reason the planet holds so much heat.",
        story:
          "I imagine wrapping Venus in layer after layer of heat-trapping fabric until the warmth has nowhere to go. Once I see it that way, its crushing atmosphere feels less abstract and much more real.",
      },
      {
        letter: "d",
        abbreviation: "CLDS",
        term: "Acid Clouds",
        definition: "The clouds of Venus contain sulfuric acid droplets.",
        explanation:
          "Its cloud tops may look beautiful from afar, but they are harsh and hostile up close.",
        story:
          "From a telescope, Venus can look smooth and elegant, almost like a glowing pearl. Then I learn those bright clouds are acidic, and suddenly the planet feels like beauty with a warning label attached.",
      },
    ],
  },
  {
    name: "Earth",
    cards: [
      {
        letter: "a",
        abbreviation: "H2O",
        term: "Surface Water",
        definition: "Earth has abundant liquid water on its surface.",
        explanation:
          "That stable water cycle is one of the biggest reasons Earth can support life so widely.",
        story:
          "I turn on a faucet or look at the ocean and usually think of it as normal. Then I remember how unusual liquid surface water may be in the solar system, and everyday water starts to feel like one of Earth's quiet miracles.",
      },
      {
        letter: "b",
        abbreviation: "AIR",
        term: "Protective Atmosphere",
        definition: "Earth's atmosphere helps us breathe, stay warm, and stay protected.",
        explanation:
          "It holds useful gases, moderates temperature, and shields life from some harmful space radiation.",
        story:
          "I step outside and barely think about the air around me. Then I realize that this invisible layer is doing the work of a life-support system every second, and the ordinary sky starts to feel like a giant gift.",
      },
      {
        letter: "c",
        abbreviation: "MOON",
        term: "Lunar Partner",
        definition: "Earth's Moon affects tides and helps steady Earth's tilt over long stretches of time.",
        explanation:
          "That steadying influence may have helped keep Earth's environment more predictable.",
        story:
          "I usually think of the Moon as something pretty hanging above me at night. Then I picture it quietly helping steady our planet, and it starts to feel less like decoration and more like a cosmic teammate.",
      },
      {
        letter: "d",
        abbreviation: "LIFE",
        term: "Living World",
        definition: "Earth is the only world we know for sure that hosts life.",
        explanation:
          "From microbes to forests to humans, life has filled Earth with astonishing variety.",
        story:
          "I walk outside, hear birds, see plants, and talk to other people without stopping to think how rare that may be. Looking at Earth through that lens makes even an ordinary afternoon feel extraordinary.",
      },
    ],
  },
  {
    name: "Mars",
    cards: [
      {
        letter: "a",
        abbreviation: "RED",
        term: "Red Dust",
        definition: "Mars looks red because its surface dust is rich in iron oxide, or rust.",
        explanation:
          "That rusty coating gives the whole planet its famous reddish color.",
        story:
          "I imagine rubbing my fingers across the ground and lifting up fine red powder like desert dust mixed with rust. Suddenly Mars feels less like a symbol in a textbook and more like a real place I could almost touch.",
      },
      {
        letter: "b",
        abbreviation: "OLY",
        term: "Olympus Mons",
        definition: "Mars hosts Olympus Mons, the largest volcano known in the solar system.",
        explanation:
          "It is so enormous that it makes even Earth's biggest mountains feel modest.",
        story:
          "I think about standing at the base of the tallest mountain I know and then realizing Olympus Mons would dwarf it. That scale makes Mars feel like a world built for giant landforms.",
      },
      {
        letter: "c",
        abbreviation: "ICE",
        term: "Polar Ice",
        definition: "Mars has polar ice caps and signs of frozen water in the ground.",
        explanation:
          "That ice is one reason scientists keep studying Mars as a place with a wetter past.",
        story:
          "I picture the red planet and then catch myself being surprised by white ice shining at the poles. That contrast makes Mars feel less like a dead red ball and more like a place with hidden history.",
      },
      {
        letter: "d",
        abbreviation: "SOL",
        term: "Similar Day",
        definition: "A Martian day is only a little longer than a day on Earth.",
        explanation:
          "One full day on Mars lasts about 24 hours and 39 minutes.",
        story:
          "I imagine moving to Mars and discovering that my daily rhythm would not be thrown completely upside down. That tiny time difference makes the planet feel oddly familiar even while everything else about it is so different.",
      },
    ],
  },
  {
    name: "Jupiter",
    cards: [
      {
        letter: "a",
        abbreviation: "GRS",
        term: "Great Red Spot",
        definition: "Jupiter's Great Red Spot is a gigantic storm that has lasted for centuries.",
        explanation:
          "It is a swirling weather system far larger than any storm we experience on Earth.",
        story:
          "I picture looking down at a storm so huge that whole Earths could fit inside its scale. That image makes Jupiter feel less like a planet and more like a living machine of motion and weather.",
      },
      {
        letter: "b",
        abbreviation: "MOON",
        term: "Moon Family",
        definition: "Jupiter has a huge collection of moons, including famous ones like Europa, Io, and Ganymede.",
        explanation:
          "Its moon system is so rich that it almost feels like a mini solar system of its own.",
        story:
          "I imagine flying toward Jupiter and realizing the planet does not arrive alone. It shows up with an entire crowd of worlds around it, and that makes the whole scene feel grander than I expected.",
      },
      {
        letter: "c",
        abbreviation: "MAG",
        term: "Magnetic Giant",
        definition: "Jupiter has an extremely powerful magnetic field.",
        explanation:
          "That magnetic environment is so intense that it shapes radiation belts around the planet.",
        story:
          "I think of magnets on my fridge and then laugh at how tiny that image is next to Jupiter. Once I imagine a magnetic field this huge, the planet starts to feel like a powerhouse instead of just a big ball of gas.",
      },
      {
        letter: "d",
        abbreviation: "GAS",
        term: "Gas Giant",
        definition: "Jupiter is a gas giant with no ordinary solid surface to stand on.",
        explanation:
          "As you go deeper, the atmosphere becomes denser and stranger instead of turning into a normal rocky ground.",
        story:
          "I picture trying to land and realizing there may be no clean moment where clouds end and solid ground begins. That makes Jupiter feel less like a destination and more like a deep, layered giant you can only enter.",
      },
    ],
  },
  {
    name: "Saturn",
    cards: [
      {
        letter: "a",
        abbreviation: "RING",
        term: "Ice Rings",
        definition: "Saturn is wrapped in a spectacular ring system made mostly of ice and rock pieces.",
        explanation:
          "Those rings are broad and bright, which is why Saturn is so instantly recognizable.",
        story:
          "I imagine seeing Saturn through a telescope for the first time and feeling like someone drew a planet and then circled it with jewelry. The rings make the whole world feel designed to impress.",
      },
      {
        letter: "b",
        abbreviation: "DENS",
        term: "Low Density",
        definition: "Saturn is so low in density that it would float in water if you had a bathtub big enough.",
        explanation:
          "That comparison is a playful way of showing how light Saturn is for its giant size.",
        story:
          "The idea sounds silly at first, but that is exactly why it sticks with me. Once I imagine an impossible cosmic bathtub, Saturn stops being just a number and becomes something I can actually remember.",
      },
      {
        letter: "c",
        abbreviation: "TIT",
        term: "Titan Moon",
        definition: "Titan, Saturn's largest moon, has a thick atmosphere and lakes of liquid hydrocarbons.",
        explanation:
          "Titan is one of the most Earth-like moons in structure while still being deeply alien.",
        story:
          "I picture a moon with weather, haze, and lakes, and for a second it almost sounds familiar. Then I remember those lakes are not water, and Titan suddenly feels like a dream version of a world rather than a normal one.",
      },
      {
        letter: "d",
        abbreviation: "HEX",
        term: "Polar Hexagon",
        definition: "Saturn has a giant hexagon-shaped weather pattern at its north pole.",
        explanation:
          "It is a real atmospheric feature, not a drawing or an illusion.",
        story:
          "I imagine looking down at the top of a planet and seeing a six-sided storm shape staring back at me. That single fact makes Saturn feel wonderfully weird in a way I never forget.",
      },
    ],
  },
  {
    name: "Uranus",
    cards: [
      {
        letter: "a",
        abbreviation: "TILT",
        term: "Sideways Tilt",
        definition: "Uranus spins on its side compared with most planets.",
        explanation:
          "Its extreme tilt makes its seasons and sunlight patterns very unusual.",
        story:
          "I imagine a spinning top that has tipped almost all the way over and somehow keeps going. That picture helps me instantly feel why Uranus behaves so differently from the other planets.",
      },
      {
        letter: "b",
        abbreviation: "METH",
        term: "Methane Tint",
        definition: "Methane in Uranus's atmosphere helps give the planet its blue-green color.",
        explanation:
          "That gas absorbs some red light, leaving the planet with its cool, calm shade.",
        story:
          "I picture sunlight arriving full and bright, then Uranus quietly filtering some of those colors away until only that pale blue-green mood remains. It makes the planet feel painted instead of merely described.",
      },
      {
        letter: "c",
        abbreviation: "YEAR",
        term: "Long Year",
        definition: "Uranus takes 84 Earth years to go once around the Sun.",
        explanation:
          "Its great distance from the Sun is why one Uranian year lasts so long.",
        story:
          "I imagine being born on Uranus and not reaching my first birthday until old age by Earth standards. That thought turns its long orbit from a fact into something I can really feel.",
      },
      {
        letter: "d",
        abbreviation: "COLD",
        term: "Deep Cold",
        definition: "Uranus is one of the coldest planets in the solar system.",
        explanation:
          "Very little heat reaches it from the Sun, and the planet also seems to leak out surprisingly little internal heat.",
        story:
          "I think of the coldest winter day I have ever felt and then imagine going so much farther beyond that it stops making sense. Uranus feels like the kind of cold that belongs to silence itself.",
      },
    ],
  },
  {
    name: "Neptune",
    cards: [
      {
        letter: "a",
        abbreviation: "WIND",
        term: "Fast Winds",
        definition: "Neptune has some of the fastest winds in the solar system.",
        explanation:
          "Its weather can whip around the planet at astonishing speeds.",
        story:
          "I imagine a storm on Earth and then picture Neptune answering, 'That is cute.' Once I compare the two in my head, Neptune starts to feel like the true king of planetary wind.",
      },
      {
        letter: "b",
        abbreviation: "TRIT",
        term: "Triton Moon",
        definition: "Neptune's moon Triton travels in a backward, or retrograde, orbit.",
        explanation:
          "That unusual motion hints that Triton may have been captured rather than forming beside Neptune.",
        story:
          "I picture a moon joining the family late and moving in the opposite direction from the usual flow. That makes Triton feel less like just another moon and more like a dramatic outsider.",
      },
      {
        letter: "c",
        abbreviation: "BLUE",
        term: "Deep Blue Look",
        definition: "Neptune is famous for its rich blue color.",
        explanation:
          "Methane helps shape that color, though the exact reason for its deeper shade is still studied.",
        story:
          "When I imagine Neptune, I do not think of a pale blue marble. I think of a deep, saturated world that feels cold, distant, and powerful all at once.",
      },
      {
        letter: "d",
        abbreviation: "YEAR",
        term: "Long Orbit",
        definition: "Neptune takes about 165 Earth years to orbit the Sun.",
        explanation:
          "Because it is so far out, its trip around the Sun is incredibly long.",
        story:
          "I imagine starting a stopwatch when Neptune begins a year and knowing that many generations on Earth would pass before that stopwatch stops. That makes the outer solar system feel truly vast.",
      },
    ],
  },
  {
    name: "Pluto",
    cards: [
      {
        letter: "a",
        abbreviation: "HEART",
        term: "Heart Plain",
        definition: "Pluto has a famous heart-shaped bright region called Tombaugh Regio.",
        explanation:
          "That feature helped Pluto become visually unforgettable after the New Horizons flyby.",
        story:
          "I think about how many distant worlds blur together in my mind, and then Pluto appears with a heart on its surface. It instantly feels more personal, almost like the solar system signed its name in a playful way.",
      },
      {
        letter: "b",
        abbreviation: "CHAR",
        term: "Charon Partner",
        definition: "Pluto and its large moon Charon orbit so closely that they act almost like a paired system.",
        explanation:
          "Charon is so big compared with Pluto that the two worlds influence each other in an unusually balanced way.",
        story:
          "I picture a small world that is not just followed by a moon but almost dances with it. That image makes Pluto and Charon feel less like parent and child and more like two partners circling together.",
      },
      {
        letter: "c",
        abbreviation: "ICE",
        term: "Frozen Surface",
        definition: "Pluto's surface includes nitrogen, methane, and carbon monoxide ice.",
        explanation:
          "Its icy chemistry helps create a landscape that is frozen but still interesting and active.",
        story:
          "I imagine a place so cold that even materials I do not normally think about can freeze solid across the ground. Pluto stops feeling simple the moment I picture a landscape built from strange ices instead of familiar stone and water.",
      },
      {
        letter: "d",
        abbreviation: "ORB",
        term: "Wide Orbit",
        definition: "Pluto takes about 248 Earth years to travel once around the Sun.",
        explanation:
          "Its long, stretched-out orbit is one reason Pluto feels so remote.",
        story:
          "I imagine sending a calendar with Pluto on it and knowing nobody on Earth today would still be waiting for its year to finish. That thought makes the outer edge of the solar system feel enormous and patient.",
      },
    ],
  },
];

const elements = {
  topicTabList: document.getElementById("topic-tab-list"),
  topicPanel: document.getElementById("topic-panel"),
  alphabetIndex: document.getElementById("alphabet-index"),
  workbookInput: document.getElementById("workbook-input"),
  workbookStatus: document.getElementById("workbook-status"),
  letterSectionTemplate: document.getElementById("letter-section-template"),
  cardTemplate: document.getElementById("card-template"),
};

let topics = [];
let activeTopicId = "";
let sectionObserver;
let cardViewportObserver;
let indexScrollSyncFrame = 0;
let snapshotStyleText = "";
const backStageOrder = ["casual", "example", "technical"];
const fieldAliases = {
  letter: ["letter", "alphabet", "alpha"],
  abbreviation: ["abbreviation", "abbr", "short form", "shortform", "acronym", "initials"],
  term: ["term", "full form", "fullform", "phrase", "expansion", "jargon", "name"],
  definition: ["definition", "short definition", "summary", "short meaning", "basic definition"],
  casual: [
    "casual",
    "casual definition",
    "plain definition",
    "simple meaning",
    "easy meaning",
    "plain meaning",
    "non technical meaning",
    "non-technical meaning",
  ],
  example: [
    "example",
    "simple example",
    "analogy",
    "story example",
    "sticky example",
    "memorable example",
    "scenario",
    "walkthrough",
  ],
  technical: [
    "technical",
    "technical explanation",
    "technical meaning",
    "formal explanation",
    "deep explanation",
    "detailed explanation",
    "technical details",
  ],
  graphType: ["graphType", "graph type", "chart type", "technical graph type", "technical chart type"],
  graphTitle: ["graphTitle", "graph title", "chart title", "technical graph title", "technical chart title"],
  graphLabels: ["graphLabels", "graph labels", "chart labels", "x labels", "chart x labels", "labels"],
  graphValues: ["graphValues", "graph values", "chart values", "y values", "chart y values", "values"],
  explanation: [
    "explanation",
    "meaning",
    "what should it mean",
    "what should it mean?",
    "plain explanation",
    "simple explanation",
    "layman explanation",
    "plain english",
    "what it means",
  ],
  story: [
    "story",
    "example story",
    "plain example",
    "layman example",
  ],
};
const positionalFields = [
  "letter",
  "abbreviation",
  "term",
  "definition",
  "explanation",
  "story",
  "casual",
  "example",
  "technical",
  "graphType",
  "graphTitle",
  "graphLabels",
  "graphValues",
];

function cloneDefaultTopics() {
  return defaultTopics.map((topic) => ({
    name: topic.name,
    cards: topic.cards.map((card) => ({ ...card })),
  }));
}

function slugify(value) {
  return String(value || "")
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function normalizeHeader(value) {
  return String(value || "")
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function toText(value) {
  return String(value ?? "")
    .replace(/\r\n/g, "\n")
    .replace(/\s+/g, " ")
    .trim();
}

function getSnapshotStyleText() {
  if (snapshotStyleText) {
    return snapshotStyleText;
  }

  snapshotStyleText = Array.from(document.styleSheets)
    .map((sheet) => {
      try {
        return Array.from(sheet.cssRules)
          .map((rule) => rule.cssText)
          .join("\n");
      } catch {
        return "";
      }
    })
    .join("\n");

  return snapshotStyleText;
}

function releaseCardSnapshot(cardNode) {
  if (cardNode._snapshot?.url) {
    URL.revokeObjectURL(cardNode._snapshot.url);
  }

  cardNode._snapshot = null;
  cardNode._snapshotPromise = null;
}

function setBackStage(cardNode, stageIndex = 0) {
  const safeStageIndex = Math.max(0, Math.min(stageIndex, backStageOrder.length - 1));
  cardNode.dataset.backStage = String(safeStageIndex);

  const activeStage = backStageOrder[safeStageIndex];
  cardNode.querySelectorAll(".back-stage").forEach((stageNode) => {
    stageNode.classList.toggle("is-active", stageNode.dataset.stage === activeStage);
  });
}

function resetCard(cardNode) {
  cardNode._burstToken = (cardNode._burstToken || 0) + 1;
  cardNode.classList.remove("is-flipped", "is-bursting");
  setBackStage(cardNode, 0);
  const fragmentLayer = cardNode.querySelector(".flash-card-fragments");
  if (fragmentLayer) {
    fragmentLayer.replaceChildren();
  }
}

function closeOtherCards(currentCardNode) {
  document.querySelectorAll(".flash-card.is-flipped, .flash-card.is-bursting").forEach((cardNode) => {
    if (cardNode !== currentCardNode) {
      resetCard(cardNode);
    }
  });
}

function observeCardsInViewport() {
  if (cardViewportObserver) {
    cardViewportObserver.disconnect();
  }

  const cards = Array.from(document.querySelectorAll(".flash-card"));

  cardViewportObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          resetCard(entry.target);
        }
      });
    },
    {
      threshold: 0.04,
    },
  );

  cards.forEach((cardNode) => cardViewportObserver.observe(cardNode));
}

async function ensureCardSnapshot(cardNode) {
  if (cardNode._snapshot) {
    return cardNode._snapshot;
  }

  if (cardNode._snapshotPromise) {
    return cardNode._snapshotPromise;
  }

  const frontFace = cardNode.querySelector(".flash-card-front");
  const { width, height } = frontFace.getBoundingClientRect();
  const snapshotWidth = Math.max(1, Math.round(width));
  const snapshotHeight = Math.max(1, Math.round(height));
  const clone = frontFace.cloneNode(true);

  clone.setAttribute("xmlns", "http://www.w3.org/1999/xhtml");
  clone.style.position = "relative";
  clone.style.inset = "auto";
  clone.style.margin = "0";
  clone.style.width = `${snapshotWidth}px`;
  clone.style.height = `${snapshotHeight}px`;
  clone.style.minHeight = `${snapshotHeight}px`;
  clone.style.opacity = "1";
  clone.style.transform = "none";
  clone.style.transition = "none";
  clone.style.boxSizing = "border-box";

  const serializedFace = new XMLSerializer().serializeToString(clone);
  const svgMarkup = `
    <svg xmlns="http://www.w3.org/2000/svg" width="${snapshotWidth}" height="${snapshotHeight}" viewBox="0 0 ${snapshotWidth} ${snapshotHeight}">
      <foreignObject width="100%" height="100%">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width:${snapshotWidth}px;height:${snapshotHeight}px;overflow:hidden;">
          <style>
            html, body {
              margin: 0;
              padding: 0;
            }
            ${getSnapshotStyleText()}
          </style>
          ${serializedFace}
        </div>
      </foreignObject>
    </svg>
  `;

  cardNode._snapshotPromise = new Promise((resolve, reject) => {
    const blob = new Blob([svgMarkup], {
      type: "image/svg+xml;charset=utf-8",
    });
    const url = URL.createObjectURL(blob);
    const image = new Image();

    image.onload = () => {
      const snapshot = {
        url,
        width: snapshotWidth,
        height: snapshotHeight,
      };
      cardNode._snapshot = snapshot;
      cardNode._snapshotPromise = null;
      resolve(snapshot);
    };

    image.onerror = () => {
      URL.revokeObjectURL(url);
      cardNode._snapshotPromise = null;
      reject(new Error("Front-face snapshot could not be created."));
    };

    image.src = url;
  });

  return cardNode._snapshotPromise;
}

function buildFragments(cardNode, snapshot) {
  const fragmentLayer = cardNode.querySelector(".flash-card-fragments");
  fragmentLayer.replaceChildren();

  const columns = Math.max(10, Math.round(snapshot.width / 20));
  const rows = Math.max(12, Math.round(snapshot.height / 18));
  const pieceWidth = snapshot.width / columns;
  const pieceHeight = snapshot.height / rows;
  const fragmentBatch = document.createDocumentFragment();

  for (let row = 0; row < rows; row += 1) {
    for (let column = 0; column < columns; column += 1) {
      const piece = document.createElement("span");
      const left = column * pieceWidth;
      const top = row * pieceHeight;
      const centerX = left + pieceWidth / 2 - snapshot.width / 2;
      const centerY = top + pieceHeight / 2 - snapshot.height / 2;
      const angle = Math.atan2(centerY || 1, centerX || 1);
      const spread = 18 + Math.random() * 26;
      const driftX = Math.cos(angle) * spread + (Math.random() - 0.5) * 18;
      const driftY = Math.sin(angle) * spread + (Math.random() - 0.5) * 22 - 10;

      piece.className = "flash-card-fragment";
      piece.style.left = `${left}px`;
      piece.style.top = `${top}px`;
      piece.style.width = `${pieceWidth + 0.8}px`;
      piece.style.height = `${pieceHeight + 0.8}px`;
      piece.style.backgroundImage = `url(${snapshot.url})`;
      piece.style.backgroundSize = `${snapshot.width}px ${snapshot.height}px`;
      piece.style.backgroundPosition = `-${left}px -${top}px`;
      piece.style.setProperty("--drift-x", `${driftX}px`);
      piece.style.setProperty("--drift-y", `${driftY}px`);
      piece.style.setProperty("--twist", `${(Math.random() - 0.5) * 50}deg`);
      piece.style.setProperty("--delay", `${Math.random() * 70}ms`);
      fragmentBatch.appendChild(piece);
    }
  }

  fragmentLayer.appendChild(fragmentBatch);
}

async function revealCard(cardNode) {
  if (cardNode.classList.contains("is-flipped")) {
    return;
  }

  const burstToken = (cardNode._burstToken || 0) + 1;
  cardNode._burstToken = burstToken;

  try {
    const snapshot = await ensureCardSnapshot(cardNode);
    if (!cardNode.isConnected || cardNode._burstToken !== burstToken) {
      return;
    }

    buildFragments(cardNode, snapshot);
    cardNode.classList.add("is-flipped");

    requestAnimationFrame(() => {
      if (cardNode._burstToken !== burstToken) {
        return;
      }

      cardNode.classList.add("is-bursting");
    });

    window.setTimeout(() => {
      if (cardNode._burstToken !== burstToken) {
        return;
      }

      cardNode.classList.remove("is-bursting");
      const fragmentLayer = cardNode.querySelector(".flash-card-fragments");
      if (fragmentLayer) {
        fragmentLayer.replaceChildren();
      }
    }, 700);
  } catch {
    cardNode.classList.add("is-flipped");
  }
}

function buildTermMarkup(term, abbreviation) {
  const words = term
    .split(/\s+/)
    .filter(Boolean);
  const normalizedAbbreviation = String(abbreviation || "")
    .replace(/[^a-z0-9]/gi, "")
    .toUpperCase();
  const initials = words.map((word) => word.charAt(0).toUpperCase()).join("");
  const shouldExpandInitials = words.length > 1 && normalizedAbbreviation && normalizedAbbreviation === initials;

  if (!shouldExpandInitials) {
    const plainTerm = document.createElement("span");
    plainTerm.className = "card-term-plain";
    plainTerm.textContent = term;
    return plainTerm;
  }

  const fragment = document.createDocumentFragment();

  words.forEach((word) => {
      const line = document.createElement("span");
      line.className = "card-term-line";

      const initial = document.createElement("span");
      initial.className = "term-initial";
      initial.textContent = word.charAt(0);

      const rest = document.createElement("span");
      rest.className = "term-rest";
      rest.textContent = word.slice(1);

      line.appendChild(initial);
      line.appendChild(rest);
      fragment.appendChild(line);
    });

  return fragment;
}

function isAbbreviationLabel(abbreviation, term) {
  const normalizedAbbreviation = String(abbreviation || "")
    .replace(/[^a-z0-9]/gi, "")
    .toUpperCase();

  if (!normalizedAbbreviation) {
    return false;
  }

  const words = String(term || "")
    .split(/\s+/)
    .filter(Boolean);

  if (words.length < 2) {
    return false;
  }

  const initials = words.map((word) => word.charAt(0).toUpperCase()).join("");
  if (normalizedAbbreviation === initials) {
    return true;
  }

  let abbreviationIndex = 0;
  for (const initial of initials) {
    if (initial === normalizedAbbreviation[abbreviationIndex]) {
      abbreviationIndex += 1;
    }
  }

  return abbreviationIndex === normalizedAbbreviation.length;
}

function buildStageSnippet(text, fallback) {
  const normalizedText = toText(text);

  if (!normalizedText) {
    return fallback;
  }

  const firstSentenceMatch = normalizedText.match(/^(.{1,170}?[.!?])(?:\s|$)/);
  const snippet = firstSentenceMatch ? firstSentenceMatch[1].trim() : normalizedText;
  return snippet.length > 170 ? `${snippet.slice(0, 167).trimEnd()}...` : snippet;
}

function splitIntoBulletItems(text) {
  const normalizedText = toText(text).replace(/\r\n?/g, "\n").trim();

  if (!normalizedText) {
    return [];
  }

  return normalizedText
    .split(/\n+/)
    .flatMap((block) =>
      block
        .split(/(?<=[.!?])\s+(?=[A-Z0-9])/)
        .map((item) => item.replace(/^[\-\u2022]\s*/, "").trim()),
    )
    .filter(Boolean);
}

function splitIntoSentences(text) {
  const normalizedText = toText(text).replace(/\s+/g, " ").trim();

  if (!normalizedText) {
    return [];
  }

  return normalizedText
    .split(/(?<=[.!?])\s+(?=[A-Z0-9])/)
    .map((sentence) => sentence.trim())
    .filter(Boolean);
}

function groupSentencesIntoParagraphs(sentences) {
  if (sentences.length <= 3) {
    return [sentences];
  }

  if (sentences.length === 4) {
    return [sentences.slice(0, 2), sentences.slice(2)];
  }

  if (sentences.length === 5) {
    return [sentences.slice(0, 3), sentences.slice(3)];
  }

  if (sentences.length === 6) {
    return [sentences.slice(0, 2), sentences.slice(2, 4), sentences.slice(4)];
  }

  return [sentences.slice(0, 3), sentences.slice(3, 6), sentences.slice(6)];
}

function renderParagraphBlocks(node, text) {
  if (!node) {
    return;
  }

  const sentences = splitIntoSentences(text);
  node.replaceChildren();

  if (!sentences.length) {
    return;
  }

  groupSentencesIntoParagraphs(sentences).forEach((group) => {
    const paragraph = document.createElement("p");
    paragraph.textContent = group.join(" ");
    node.appendChild(paragraph);
  });
}

function renderExampleBullets(node, text) {
  if (!node) {
    return;
  }

  const bulletItems = splitIntoBulletItems(text);
  node.replaceChildren();

  if (!bulletItems.length) {
    return;
  }

  const list = document.createElement("ul");
  list.className = "example-bullet-list";
  const usedIcons = new Set();

  bulletItems.forEach((item, index) => {
    const listItem = document.createElement("li");
    const iconClass = classifyExampleBullet(item, index);
    listItem.classList.add(iconClass);
    listItem.dataset.icon = iconForBulletClass(iconClass, item, index, usedIcons);
    listItem.dataset.step = String(index + 1).padStart(2, "0");
    listItem.textContent = item;
    list.appendChild(listItem);
  });

  node.appendChild(list);
}

function classifyExampleBullet(text, index = 0) {
  const normalizedText = toText(text).toLowerCase();

  if (/(trailer|stream|streaming|video|watch|screen|episode|series|monitor|display)/.test(normalizedText)) {
    return "icon-screen";
  }

  if (/(spotify|music|song|album|playlist|audio|concert|artist|label|band|podcast|singer|guitar)/.test(normalizedText)) {
    return "icon-music";
  }

  if (/(netflix|disney|movie|film|stream|trailer|box office|studio|title|episode|series|cinema|premiere|director|camera)/.test(normalizedText)) {
    return "icon-movie";
  }

  if (/(airport|airline|flight|aircraft|boeing|delta|hangar|gate|plane|jet|runway|boarding|landing|takeoff)/.test(normalizedText)) {
    return "icon-flight";
  }

  if (/(charging|battery|supercharger|electric|powertrain|plug|socket|voltage|current|watt)/.test(normalizedText)) {
    return "icon-battery";
  }

  if (/(software|app|platform|cloud|device|server|apple|tech|phone|mobile|laptop|computer|portal|website)/.test(normalizedText)) {
    return "icon-tech";
  }

  if (/(japan|tokyo|osaka|yokohama|port|harbor|shipping|cargo|container|ship|sea|ocean|import|export|vessel|freight)/.test(normalizedText)) {
    return "icon-ship";
  }

  if (/(truck|transport|transit|fleet|route|lane|distance|mile|road|corridor|highway|path|rail|train|subway|bus|car|taxi|uber|van)/.test(normalizedText)) {
    return "icon-route";
  }

  if (/(parcel|package|shipment|box|delivery|courier|mail|post)/.test(normalizedText)) {
    return "icon-package";
  }

  if (/(warehouse|hub|sort|dispatch|fulfillment|inventory|dock|loading|storage)/.test(normalizedText)) {
    return "icon-warehouse";
  }

  if (
    /(store|retail|shop|checkout|customer|promotion|walmart|costco|shelf|aisle|mall|market|restaurant|coffee|tea|pizza|burger|fruit|snack|lunch|dinner|breakfast)/.test(
      normalizedText,
    )
  ) {
    return "icon-retail";
  }

  if (/(price|cost|revenue|sales|rent|fare|budget|profit|spend|cash|payment|invoice|card|dollar)/.test(normalizedText)) {
    return "icon-money";
  }

  if (/(weather|storm|rain|snow|wind|sun|holiday|season|cloud|summer|winter)/.test(normalizedText)) {
    return "icon-weather";
  }

  if (/(delay|time|minute|hour|arrival|departure|schedule|week|day|month|quarter|clock|calendar|timeline)/.test(normalizedText)) {
    return "icon-time";
  }

  if (/(team|manager|staff|crew|operator|planner|group|partner|colleague|analyst)/.test(normalizedText)) {
    return "icon-team";
  }

  if (/(check|compare|review|inspect|verify|confirm|audit|test|validate)/.test(normalizedText)) {
    return "icon-check";
  }

  if (
    /(amazon|ups|fedex|delivery|route|parcel|warehouse|truck|logistics|dispatch|hub|sort)/.test(
      normalizedText,
    )
  ) {
    return "icon-route";
  }

  if (/(model|predict|estimate|coefficient|residual|line|data|variable|regression|metric|forecast|fit|graph|chart|trend|analysis)/.test(normalizedText)) {
    return "icon-chart";
  }

  const fallbacks = ["icon-flow", "icon-compass", "icon-pin", "icon-spark"];
  return fallbacks[index % fallbacks.length];
}

function pushUniqueEmoji(list, ...icons) {
  icons.flat().forEach((icon) => {
    if (icon && !list.includes(icon)) {
      list.push(icon);
    }
  });
}

function emojiOptionsForBulletClass(iconClass, text = "", index = 0) {
  const normalizedText = toText(text).toLowerCase();
  const icons = [];

  if (iconClass === "icon-screen") {
    if (/(screen|monitor|display|dashboard)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🖥️", "📺", "🎞️", "🎛️");
      return icons;
    }
    if (/(stream|streaming|watch|episode|series|video)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "📺", "🎞️", "🎬", "🖥️");
      return icons;
    }
    pushUniqueEmoji(icons, "📺", "🖥️", "🎞️", "🎛️");
    return icons;
  }

  if (iconClass === "icon-music") {
    if (/(headphone|audio|podcast|listen)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🎧", "🎙️", "🎵", "📻");
      return icons;
    }
    if (/(guitar|band)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🎸", "🥁", "🎤", "🎵");
      return icons;
    }
    if (/(concert|singer|mic|microphone)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🎤", "🎶", "🎧", "🎵");
      return icons;
    }
    pushUniqueEmoji(icons, "🎵", "🎧", "🎸", "🎤", "🎙️", "📻");
    return icons;
  }

  if (iconClass === "icon-movie") {
    if (/(netflix|popcorn)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🍿", "🎬", "📺", "🎞️");
      return icons;
    }
    if (/(trailer|screen|watch|stream|episode|series)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "📺", "🎞️", "🎬", "🍿");
      return icons;
    }
    if (/(movie|film|cinema|studio|premiere|director|camera)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🎬", "🎥", "🎞️", "🍿");
      return icons;
    }
    pushUniqueEmoji(icons, "🎬", "🍿", "📺", "🎞️", "🎥");
    return icons;
  }

  if (iconClass === "icon-flight") {
    if (/(departure|takeoff|boarding|gate)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🛫", "✈️", "🧳", "🛬");
      return icons;
    }
    if (/(arrival|landing|touchdown)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🛬", "✈️", "🧳", "🛫");
      return icons;
    }
    pushUniqueEmoji(icons, "✈️", "🛫", "🛬", "🧳", "🛩️");
    return icons;
  }

  if (iconClass === "icon-battery") {
    if (/(plug|socket|charger)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🔌", "⚡", "🔋");
      return icons;
    }
    if (/(electric|power|voltage|current|watt)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "⚡", "🔋", "🔌");
      return icons;
    }
    pushUniqueEmoji(icons, "🔋", "⚡", "🔌");
    return icons;
  }

  if (iconClass === "icon-tech") {
    if (/(phone|mobile|app)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "📱", "💻", "🖥️", "⌚");
      return icons;
    }
    if (/(server|cloud)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "☁️", "🖥️", "💻", "📡");
      return icons;
    }
    if (/(laptop|computer|device|software|platform|tech)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "💻", "🖥️", "📱", "☁️");
      return icons;
    }
    pushUniqueEmoji(icons, "💻", "📱", "🖥️", "☁️", "📡", "⌚");
    return icons;
  }

  if (iconClass === "icon-ship") {
    if (/(japan|tokyo|osaka|yokohama)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🗾", "🚢", "⚓", "🌊");
      return icons;
    }
    if (/(port|harbor|anchor)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "⚓", "🚢", "🌊", "🗾");
      return icons;
    }
    pushUniqueEmoji(icons, "🚢", "⚓", "🗾", "🌊", "🛳️");
    return icons;
  }

  if (iconClass === "icon-route") {
    if (/(truck|delivery|freight|fleet|highway|van)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🚚", "🚛", "🛣️", "🗺️");
      return icons;
    }
    if (/(train|rail|subway)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🚆", "🚉", "🗺️", "🚚");
      return icons;
    }
    if (/(bus|coach)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🚌", "🚏", "🗺️", "🚗");
      return icons;
    }
    if (/(car|taxi|uber)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🚗", "🚕", "🗺️", "🛣️");
      return icons;
    }
    if (/(route|road|lane|corridor|path|distance|mile)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🗺️", "🛣️", "🚚", "🚗");
      return icons;
    }
    pushUniqueEmoji(icons, "🚚", "🚛", "🚆", "🚌", "🚗", "🚕", "🗺️", "🛣️");
    return icons;
  }

  if (iconClass === "icon-package") {
    if (/(mail|post|courier)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "📬", "📦", "🏷️", "✉️");
      return icons;
    }
    if (/(label|tag)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🏷️", "📦", "📬", "✉️");
      return icons;
    }
    pushUniqueEmoji(icons, "📦", "📬", "🏷️", "✉️");
    return icons;
  }

  if (iconClass === "icon-warehouse") {
    if (/(inventory|storage)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🗃️", "🏬", "🏭", "📦");
      return icons;
    }
    if (/(hub|warehouse|fulfillment)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🏬", "🏭", "🗃️", "📦");
      return icons;
    }
    pushUniqueEmoji(icons, "🏭", "🏬", "🗃️", "📦");
    return icons;
  }

  if (iconClass === "icon-retail") {
    if (/(coffee|tea)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "☕", "🛍️", "🏪", "🍩");
      return icons;
    }
    if (/(pizza|restaurant|slice)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🍕", "🍽️", "🛍️", "🍔");
      return icons;
    }
    if (/(burger|snack|lunch|dinner|breakfast)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🍔", "🍟", "🍽️", "🛍️");
      return icons;
    }
    if (/(fruit|apple)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🍎", "🍊", "🛍️", "🏪");
      return icons;
    }
    if (/(checkout|cart)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🛒", "🛍️", "💳", "🏪");
      return icons;
    }
    if (/(shop|store|market|customer|promotion|mall)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🛍️", "🏪", "🛒", "🏬");
      return icons;
    }
    pushUniqueEmoji(icons, "🛒", "🛍️", "🏪", "🏬", "🍎", "☕");
    return icons;
  }

  if (iconClass === "icon-money") {
    if (/(card|payment)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "💳", "💵", "💰", "🧾");
      return icons;
    }
    if (/(profit|revenue|sales|budget|cash)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "💰", "💵", "📈", "🧾");
      return icons;
    }
    pushUniqueEmoji(icons, "💵", "💰", "💳", "🧾");
    return icons;
  }

  if (iconClass === "icon-weather") {
    if (/(rain|storm)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🌧️", "⛈️", "🌦️", "☔");
      return icons;
    }
    if (/(snow|winter)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "❄️", "☃️", "🌨️", "🌬️");
      return icons;
    }
    if (/(sun|summer|holiday)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "☀️", "🌤️", "🌴", "😎");
      return icons;
    }
    pushUniqueEmoji(icons, "☀️", "🌧️", "⛈️", "❄️", "🌤️", "☔");
    return icons;
  }

  if (iconClass === "icon-time") {
    if (/(calendar|week|day|month|quarter)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "📅", "🗓️", "🕒", "⏱️");
      return icons;
    }
    if (/(schedule|clock|time|minute|hour|timeline)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🕒", "⏱️", "⏰", "📅");
      return icons;
    }
    pushUniqueEmoji(icons, "⏱️", "🕒", "⏰", "📅", "🗓️");
    return icons;
  }

  if (iconClass === "icon-team") {
    if (/(partner|colleague|manager)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🤝", "👥", "🧑‍🤝‍🧑");
      return icons;
    }
    if (/(team|crew|group|staff)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "👥", "🧑‍🤝‍🧑", "🤝");
      return icons;
    }
    pushUniqueEmoji(icons, "👥", "🤝", "🧑‍🤝‍🧑");
    return icons;
  }

  if (iconClass === "icon-check") {
    if (/(inspect|verify|review|audit)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "🔎", "✅", "📋", "🧪");
      return icons;
    }
    if (/(test|validate|confirm|check)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "✅", "🧪", "📋", "🔎");
      return icons;
    }
    pushUniqueEmoji(icons, "✅", "🔎", "📋", "🧪");
    return icons;
  }

  if (iconClass === "icon-chart") {
    if (/(graph|trend|forecast)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "📈", "📊", "🧮", "📉");
      return icons;
    }
    if (/(data|analysis|metric)/.test(normalizedText)) {
      pushUniqueEmoji(icons, "📊", "🧮", "📈", "📉");
      return icons;
    }
    pushUniqueEmoji(icons, "📈", "📊", "🧮", "📉");
    return icons;
  }

  if (iconClass === "icon-compass") {
    pushUniqueEmoji(icons, "🧭", "🗺️", "📍");
    return icons;
  }

  if (iconClass === "icon-pin") {
    pushUniqueEmoji(icons, "📍", "🧭", "🗺️");
    return icons;
  }

  if (iconClass === "icon-spark") {
    pushUniqueEmoji(icons, "✨", "💡", "🌟");
    return icons;
  }

  pushUniqueEmoji(icons, "➡️", "🧭", "📍", "✨", "💡");
  return icons;
}

function iconForBulletClass(iconClass, text = "", index = 0, usedIcons = new Set()) {
  const options = emojiOptionsForBulletClass(iconClass, text, index);

  if (!options.length) {
    return "➡️";
  }

  const unusedOption = options.find((option) => !usedIcons.has(option));
  const selected = unusedOption || options[index % options.length];
  usedIcons.add(selected);
  return selected;
}

function splitChartList(value) {
  const normalizedValue = toText(value);

  if (!normalizedValue) {
    return [];
  }

  if (normalizedValue.startsWith("[") && normalizedValue.endsWith("]")) {
    try {
      const parsed = JSON.parse(normalizedValue);
      if (Array.isArray(parsed)) {
        return parsed.map((item) => toText(item)).filter(Boolean);
      }
    } catch {
      // Fall through to delimiter parsing.
    }
  }

  if (normalizedValue.includes("|")) {
    return normalizedValue
      .split("|")
      .map((item) => toText(item))
      .filter(Boolean);
  }

  if (normalizedValue.includes("\n")) {
    return normalizedValue
      .split(/\n+/)
      .map((item) => toText(item))
      .filter(Boolean);
  }

  if (normalizedValue.includes(";")) {
    return normalizedValue
      .split(";")
      .map((item) => toText(item))
      .filter(Boolean);
  }

  return normalizedValue
    .split(",")
    .map((item) => toText(item))
    .filter(Boolean);
}

function parseChartNumber(value) {
  const normalizedValue = String(value ?? "").trim();
  if (!normalizedValue) {
    return null;
  }

  const parsedValue = Number.parseFloat(normalizedValue.replace(/[^0-9.+-]/g, ""));
  return Number.isFinite(parsedValue) ? parsedValue : null;
}

function createSvgNode(name, attributes = {}) {
  const node = document.createElementNS("http://www.w3.org/2000/svg", name);
  Object.entries(attributes).forEach(([attribute, value]) => {
    node.setAttribute(attribute, String(value));
  });
  return node;
}

function buildChartConfig(card) {
  const values = splitChartList(card.graphValues)
    .map((value) => parseChartNumber(value))
    .filter((value) => value !== null);

  if (!values.length) {
    return null;
  }

  const labels = splitChartList(card.graphLabels);
  const itemCount = values.length;
  const normalizedLabels = Array.from({ length: itemCount }, (_, index) => labels[index] || `Step ${index + 1}`);
  const normalizedType = toText(card.graphType).toLowerCase();

  return {
    type: normalizedType === "line" ? "line" : "bar",
    title: toText(card.graphTitle),
    labels: normalizedLabels,
    values,
  };
}

function buildTechnicalChart(card, theme) {
  const chartConfig = buildChartConfig(card);
  if (!chartConfig) {
    return null;
  }

  const width = 360;
  const height = 220;
  const paddingLeft = 34;
  const paddingRight = 16;
  const paddingTop = 18;
  const paddingBottom = 40;
  const plotWidth = width - paddingLeft - paddingRight;
  const plotHeight = height - paddingTop - paddingBottom;
  const maxValue = Math.max(...chartConfig.values, 1);
  const figure = document.createElement("figure");
  figure.className = "technical-chart";

  if (chartConfig.title) {
    const caption = document.createElement("figcaption");
    caption.className = "technical-chart-title";
    caption.textContent = chartConfig.title;
    figure.appendChild(caption);
  }

  const svg = createSvgNode("svg", {
    class: "technical-chart-graphic",
    viewBox: `0 0 ${width} ${height}`,
    role: "img",
    "aria-label": chartConfig.title || "Technical chart",
  });

  [0.25, 0.5, 0.75, 1].forEach((ratio) => {
    const y = paddingTop + plotHeight - plotHeight * ratio;
    svg.appendChild(
      createSvgNode("line", {
        x1: paddingLeft,
        y1: y,
        x2: width - paddingRight,
        y2: y,
        stroke: "rgba(24, 34, 47, 0.12)",
        "stroke-width": 1,
      }),
    );
  });

  svg.appendChild(
    createSvgNode("line", {
      x1: paddingLeft,
      y1: paddingTop + plotHeight,
      x2: width - paddingRight,
      y2: paddingTop + plotHeight,
      stroke: "rgba(24, 34, 47, 0.22)",
      "stroke-width": 1.4,
    }),
  );

  if (chartConfig.type === "line") {
    const points = chartConfig.values.map((value, index) => {
      const x = paddingLeft + (plotWidth * index) / Math.max(chartConfig.values.length - 1, 1);
      const y = paddingTop + plotHeight - (value / maxValue) * plotHeight;
      return { x, y, value, label: chartConfig.labels[index] };
    });

    svg.appendChild(
      createSvgNode("polyline", {
        points: points.map(({ x, y }) => `${x},${y}`).join(" "),
        fill: "none",
        stroke: theme.accentStrong,
        "stroke-width": 4,
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
      }),
    );

    points.forEach(({ x, y }) => {
      svg.appendChild(
        createSvgNode("circle", {
          cx: x,
          cy: y,
          r: 4.5,
          fill: theme.accent,
          stroke: "#ffffff",
          "stroke-width": 2,
        }),
      );
    });
  } else {
    const columnWidth = plotWidth / chartConfig.values.length;
    chartConfig.values.forEach((value, index) => {
      const barHeight = (value / maxValue) * plotHeight;
      const x = paddingLeft + columnWidth * index + columnWidth * 0.16;
      const y = paddingTop + plotHeight - barHeight;
      svg.appendChild(
        createSvgNode("rect", {
          x,
          y,
          width: columnWidth * 0.68,
          height: barHeight,
          rx: 8,
          fill: theme.accent,
          opacity: 0.9,
        }),
      );
    });
  }

  chartConfig.labels.forEach((label, index) => {
    const x =
      chartConfig.type === "line"
        ? paddingLeft + (plotWidth * index) / Math.max(chartConfig.labels.length - 1, 1)
        : paddingLeft + (plotWidth / chartConfig.labels.length) * index + plotWidth / chartConfig.labels.length / 2;
    const text = createSvgNode("text", {
      x,
      y: height - 14,
      fill: "rgba(24, 34, 47, 0.75)",
      "font-size": 10,
      "font-family": "Avenir Next, Trebuchet MS, sans-serif",
      "text-anchor": "middle",
    });
    text.textContent = label.length > 10 ? `${label.slice(0, 9)}…` : label;
    svg.appendChild(text);
  });

  figure.appendChild(svg);
  return figure;
}

function buildCardTheme(cardIndex) {
  const hue = (cardIndex * 137.508) % 360;
  return {
    accent: `hsl(${hue} 72% 44%)`,
    accentStrong: `hsl(${hue} 74% 28%)`,
    accentShadow: `hsl(${hue} 62% 18%)`,
    badgeStart: `hsl(${hue} 78% 90%)`,
    badgeEnd: `hsl(${hue} 72% 82%)`,
    definitionStart: `hsl(${hue} 82% 96%)`,
    definitionEnd: `hsl(${hue} 70% 90%)`,
    meaningStart: `hsl(${hue} 84% 93%)`,
    meaningEnd: `hsl(${hue} 76% 86%)`,
    heading: `hsl(${hue} 68% 32%)`,
  };
}

function createCard(card, cardIndex) {
  const cardNode = elements.cardTemplate.content.firstElementChild.cloneNode(true);
  const theme = buildCardTheme(cardIndex);
  const hasBackStages = Boolean(cardNode.querySelector(".back-stage"));
  const usesAbbreviation = isAbbreviationLabel(card.abbreviation, card.term);
  const frontLeadLabel = usesAbbreviation ? card.abbreviation : card.term;
  const backChipLabel = usesAbbreviation ? card.abbreviation : card.term;
  const frontMainNode = cardNode.querySelector(".card-front-main");
  const frontCopyNode = cardNode.querySelector(".card-term");
  const frontBadgeNode = cardNode.querySelector(".card-abbreviation");
  const frontBadgeBlock = cardNode.querySelector(".card-front-badge");
  const frontCopyBlock = cardNode.querySelector(".card-front-copy");

  cardNode.dataset.letter = card.letter;
  cardNode.style.setProperty("--example-accent", theme.accent);
  cardNode.style.setProperty("--back-chip-bg", theme.accent);
  cardNode.style.setProperty("--back-chip-ink", "#ffffff");
  cardNode.style.setProperty("--meaning-bg-start", theme.meaningStart);
  cardNode.style.setProperty("--meaning-bg-end", theme.meaningEnd);
  cardNode.style.setProperty("--meaning-heading", theme.heading);
  cardNode.style.setProperty("--front-accent", theme.accent);
  cardNode.style.setProperty("--front-accent-strong", theme.accentStrong);
  cardNode.style.setProperty("--front-accent-shadow", theme.accentShadow);
  cardNode.style.setProperty("--front-badge-start", theme.badgeStart);
  cardNode.style.setProperty("--front-badge-end", theme.badgeEnd);
  cardNode.style.setProperty("--front-definition-start", theme.definitionStart);
  cardNode.style.setProperty("--front-definition-end", theme.definitionEnd);
  cardNode.style.setProperty("--casual-panel-start", theme.meaningStart);
  cardNode.style.setProperty("--casual-panel-end", theme.meaningEnd);
  cardNode.style.setProperty("--casual-panel-border", theme.heading);
  cardNode.style.setProperty("--example-panel-start", theme.badgeStart);
  cardNode.style.setProperty("--example-panel-end", theme.badgeEnd);
  cardNode.style.setProperty("--example-panel-border", theme.accent);
  cardNode.style.setProperty("--technical-panel-start", theme.definitionStart);
  cardNode.style.setProperty("--technical-panel-end", theme.definitionEnd);
  cardNode.style.setProperty("--technical-panel-border", theme.accentStrong);

  setBackStage(cardNode, 0);
  cardNode.querySelector(".flash-card-back .card-chip").textContent = backChipLabel;
  cardNode.querySelector(".flash-card-back .card-chip").classList.toggle("is-term-chip", !usesAbbreviation);
  frontMainNode.classList.toggle("is-concept-only", !usesAbbreviation);
  frontBadgeNode.textContent = frontLeadLabel;
  frontBadgeNode.classList.toggle("is-term-label", !usesAbbreviation);
  frontBadgeBlock.classList.toggle("is-term-badge", !usesAbbreviation);
  frontCopyBlock.classList.toggle("is-note-block", false);
  frontCopyNode.classList.toggle("is-note", false);

  if (usesAbbreviation) {
    frontCopyNode.replaceChildren(buildTermMarkup(card.term, card.abbreviation));
  } else {
    frontCopyNode.replaceChildren();
  }

  const definitionNode = cardNode.querySelector(".card-definition");
  const casualNode = cardNode.querySelector(".card-casual");
  const exampleNode = cardNode.querySelector(".card-example");
  const technicalNode = cardNode.querySelector(".card-technical");
  const technicalChartSlot = cardNode.querySelector(".technical-chart-slot");
  const casualSnippetNode = cardNode.querySelector(".card-casual-snippet");
  const exampleSnippetNode = cardNode.querySelector(".card-example-snippet");
  const technicalSnippetNode = cardNode.querySelector(".card-technical-snippet");

  if (definitionNode) {
    definitionNode.textContent = card.definition;
  }

  if (casualNode) {
    renderParagraphBlocks(casualNode, card.casual);
  }

  if (exampleNode) {
    renderExampleBullets(exampleNode, card.example);
  }

  if (technicalNode) {
    renderParagraphBlocks(technicalNode, card.technical);
  }

  if (technicalChartSlot) {
    const chartNode = buildTechnicalChart(card, theme);
    technicalChartSlot.replaceChildren();
    technicalChartSlot.classList.toggle("has-chart", Boolean(chartNode));
    if (chartNode) {
      technicalChartSlot.appendChild(chartNode);
    }
  }

  if (casualSnippetNode) {
    casualSnippetNode.textContent = buildStageSnippet(
      card.casual,
      "A plain-language way to hold the idea before the technical layer shows up.",
    );
  }

  if (exampleSnippetNode) {
    exampleSnippetNode.textContent = buildStageSnippet(
      card.example,
      "A sticky everyday picture that helps the concept stay in memory.",
    );
  }

  if (technicalSnippetNode) {
    technicalSnippetNode.textContent = buildStageSnippet(
      card.technical,
      "A more exact explanation that names the mechanism more precisely.",
    );
  }

  const toggleCard = () => {
    if (cardNode.classList.contains("is-bursting")) {
      return;
    }

    if (cardNode.classList.contains("is-flipped")) {
      if (!hasBackStages) {
        resetCard(cardNode);
        return;
      }

      const currentStageIndex = Number(cardNode.dataset.backStage || 0);
      if (currentStageIndex >= backStageOrder.length - 1) {
        resetCard(cardNode);
      } else {
        setBackStage(cardNode, currentStageIndex + 1);
      }
      return;
    }

    closeOtherCards(cardNode);
    setBackStage(cardNode, 0);
    revealCard(cardNode);
  };

  cardNode.addEventListener("click", toggleCard);
  cardNode.addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      toggleCard();
    }

    if (event.key === "Escape") {
      resetCard(cardNode);
    }
  });

  return {
    node: cardNode,
    theme,
  };
}

function getTopicOffset(topicId) {
  return topics.findIndex((topic) => topic.id === topicId) * 100;
}

function getTopicById(topicId) {
  return topics.find((topic) => topic.id === topicId);
}

function buildTopicTabs() {
  const fragment = document.createDocumentFragment();

  topics.forEach((topic, index) => {
    const tab = document.createElement("button");
    const theme = buildCardTheme(index * 100);
    tab.className = "topic-tab";
    tab.id = `tab-${topic.id}`;
    tab.type = "button";
    tab.role = "tab";
    tab.dataset.topic = topic.id;
    tab.setAttribute("aria-controls", "topic-panel");
    tab.setAttribute("aria-selected", String(topic.id === activeTopicId));
    tab.setAttribute("aria-label", topic.name);
    tab.textContent = topic.name.toLowerCase();
    tab.style.setProperty("--topic-chip-start", theme.badgeStart);
    tab.style.setProperty("--topic-chip-end", theme.badgeEnd);
    tab.style.setProperty("--topic-chip-ink", theme.heading);
    tab.addEventListener("click", () => {
      renderTopic(topic.id);
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    fragment.appendChild(tab);
  });

  elements.topicTabList.replaceChildren(fragment);
}

function buildAlphabetIndex(sectionEntries) {
  const fragment = document.createDocumentFragment();
  sectionEntries.forEach(({ sectionId, label, theme }, index) => {
    const link = document.createElement("a");
    link.className = "alphabet-link";
    link.href = `#${sectionId}`;
    link.dataset.target = sectionId;
    link.dataset.index = String(index + 1).padStart(2, "0");
    link.textContent = label;
    link.title = label;
    link.setAttribute("aria-label", `Jump to ${link.dataset.index}. ${label}`);
    link.style.setProperty("--letter-bg-start", theme.badgeStart);
    link.style.setProperty("--letter-bg-end", theme.badgeEnd);
    fragment.appendChild(link);
  });

  elements.alphabetIndex.replaceChildren(fragment);
  scheduleIndexScrollSync();
}

function syncAlphabetIndexScroll() {
  const indexNode = elements.alphabetIndex;
  if (!indexNode) {
    return;
  }

  const maxScroll = indexNode.scrollHeight - indexNode.clientHeight;
  if (maxScroll <= 1) {
    indexNode.scrollTop = 0;
    return;
  }

  const sections = Array.from(document.querySelectorAll(".letter-section"));
  if (!sections.length) {
    indexNode.scrollTop = 0;
    return;
  }

  const viewportHeight = window.innerHeight || document.documentElement.clientHeight || 1;
  const scrollTop = window.scrollY || window.pageYOffset || 0;
  const firstTop = sections[0].getBoundingClientRect().top + scrollTop;
  const lastBottom = sections[sections.length - 1].getBoundingClientRect().bottom + scrollTop;
  const start = Math.max(0, firstTop - viewportHeight * 0.22);
  const end = Math.max(start + 1, lastBottom - viewportHeight * 0.78);
  const progress = Math.min(1, Math.max(0, (scrollTop - start) / (end - start)));

  indexNode.scrollTop = maxScroll * progress;
}

function scheduleIndexScrollSync() {
  if (indexScrollSyncFrame) {
    return;
  }

  indexScrollSyncFrame = window.requestAnimationFrame(() => {
    indexScrollSyncFrame = 0;
    syncAlphabetIndexScroll();
  });
}

function observeSections() {
  if (sectionObserver) {
    sectionObserver.disconnect();
  }

  const links = Array.from(document.querySelectorAll(".alphabet-link"));
  const sections = Array.from(document.querySelectorAll(".letter-section"));

  sectionObserver = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((left, right) => right.intersectionRatio - left.intersectionRatio)[0];

      if (!visible) {
        return;
      }

      const visibleTarget = visible.target.dataset.target;
      links.forEach((link) => {
        link.classList.toggle("is-active", link.dataset.target === visibleTarget);
      });
      scheduleIndexScrollSync();
    },
    {
      rootMargin: "-10% 0px -70% 0px",
      threshold: [0.15, 0.4, 0.7],
    },
  );

  sections.forEach((section) => sectionObserver.observe(section));
}

function renderTopic(topicId) {
  const topic = getTopicById(topicId);

  if (!topic) {
    return;
  }

  activeTopicId = topicId;

  Array.from(elements.topicPanel.querySelectorAll(".flash-card")).forEach((cardNode) => {
    resetCard(cardNode);
    releaseCardSnapshot(cardNode);
  });

  const fragment = document.createDocumentFragment();
  const sectionEntries = [];
  let cardIndex = getTopicOffset(topicId);
  const usedSectionIds = new Set();

  topic.cards.forEach((card, index) => {
    const sectionNode = elements.letterSectionTemplate.content.firstElementChild.cloneNode(true);
    let sectionId = `${topicId}-${slugify(card.term || card.abbreviation || card.letter || `card-${index + 1}`)}`;
    let suffix = 2;
    while (usedSectionIds.has(sectionId)) {
      sectionId = `${topicId}-${slugify(card.term || card.abbreviation || card.letter || `card-${index + 1}`)}-${suffix}`;
      suffix += 1;
    }
    usedSectionIds.add(sectionId);
    sectionNode.id = sectionId;
    sectionNode.dataset.target = sectionId;
    sectionNode.style.animationDelay = `${Math.min(index * 28, 420)}ms`;

    const grid = sectionNode.querySelector(".card-grid");
    const sectionTheme = buildCardTheme(cardIndex);
    sectionEntries.push({
      sectionId,
      label: card.term,
      theme: sectionTheme,
    });

    const cardRender = createCard(card, cardIndex);
    grid.appendChild(cardRender.node);
    cardIndex += 1;

    fragment.appendChild(sectionNode);
  });

  buildAlphabetIndex(sectionEntries);
  elements.topicPanel.replaceChildren(fragment);

  Array.from(elements.topicTabList.querySelectorAll(".topic-tab")).forEach((tab) => {
    const isSelected = tab.dataset.topic === topicId;
    tab.classList.toggle("is-active", isSelected);
    tab.setAttribute("aria-selected", String(isSelected));
  });

  const activeTab = document.getElementById(`tab-${topicId}`);
  if (activeTab) {
    elements.topicPanel.setAttribute("aria-labelledby", activeTab.id);
  }

  observeSections();
  observeCardsInViewport();

  const firstLink = document.querySelector(".alphabet-link");
  if (firstLink) {
    firstLink.classList.add("is-active");
  }

  scheduleIndexScrollSync();
}

function setStatus(message, tone = "default") {
  elements.workbookStatus.textContent = message;
  elements.workbookStatus.classList.remove("is-error", "is-success", "is-hidden");

  if (tone === "error") {
    elements.workbookStatus.classList.add("is-error");
  }

  if (tone === "success") {
    elements.workbookStatus.classList.add("is-success");
  }
}

function clearStatus() {
  elements.workbookStatus.textContent = "";
  elements.workbookStatus.classList.remove("is-error", "is-success");
  elements.workbookStatus.classList.add("is-hidden");
}

function normalizeTopics(rawTopics) {
  const usedIds = new Set();

  return rawTopics
    .map((topic, index) => {
      const cards = (topic.cards || [])
        .map((card, cardIndex) => ({
          letter: slugify(card.letter || "").charAt(0),
          abbreviation: toText(card.abbreviation),
          term: toText(card.term),
          definition: toText(
            card.definition ||
              card.casual ||
              card.explanation ||
              card.technical ||
              card.story ||
              card.example,
          ),
          casual: toText(card.casual || card.definition || card.explanation || card.technical),
          example: toText(card.example || card.story || card.definition || card.explanation),
          technical: toText(card.technical || card.explanation || card.definition),
          graphType: toText(card.graphType),
          graphTitle: toText(card.graphTitle),
          graphLabels: toText(card.graphLabels),
          graphValues: toText(card.graphValues),
          _rowIndex: card._rowIndex ?? cardIndex,
        }))
        .filter((card) => card.letter && card.term && card.definition);

      if (!cards.length) {
        return null;
      }

      let id = slugify(topic.name) || `topic-${index + 1}`;
      let suffix = 2;
      while (usedIds.has(id)) {
        id = `${slugify(topic.name) || `topic-${index + 1}`}-${suffix}`;
        suffix += 1;
      }
      usedIds.add(id);

      return {
        id,
        name: toText(topic.name) || `Topic ${index + 1}`,
        cards,
      };
    })
    .filter(Boolean);
}

function setTopics(rawTopics, statusMessage) {
  const normalizedTopics = normalizeTopics(rawTopics);

  if (!normalizedTopics.length) {
    throw new Error(
      "No usable sheets were found in that workbook. Use a header row with columns like letter, abbreviation, term, definition, casual, example, technical, or use the older explanation and story columns as fallbacks.",
    );
  }

  topics = normalizedTopics;
  const nextActiveTopic = normalizedTopics.some((topic) => topic.id === activeTopicId)
    ? activeTopicId
    : normalizedTopics[0].id;

  activeTopicId = nextActiveTopic;
  buildTopicTabs();
  renderTopic(activeTopicId);

  if (statusMessage) {
    setStatus(statusMessage, "success");
  }
}

function pickValue(record, aliases) {
  for (const alias of aliases) {
    if (record[alias]) {
      return record[alias];
    }
  }

  return "";
}

function canonicalFieldName(headerValue) {
  const normalizedValue = normalizeHeader(headerValue);
  return (
    Object.entries(fieldAliases).find(([, aliases]) => aliases.includes(normalizedValue))?.[0] || ""
  );
}

function findHeaderRowIndex(rows) {
  const scanLimit = Math.min(rows.length, 8);

  for (let index = 0; index < scanLimit; index += 1) {
    const recognizedFields = new Set(
      rows[index]
        .map((value) => canonicalFieldName(value))
        .filter(Boolean),
    );

    if (
      recognizedFields.size >= 2 &&
      (recognizedFields.has("abbreviation") || recognizedFields.has("term") || recognizedFields.has("definition"))
    ) {
      return index;
    }
  }

  return -1;
}

function buildRowMapping(headerRow) {
  return headerRow.map((value) => canonicalFieldName(value));
}

function buildPositionalMapping(rowLength) {
  return Array.from({ length: rowLength }, (_, index) => positionalFields[index] || "");
}

function buildRecordFromRow(row, mapping) {
  const record = {};

  mapping.forEach((fieldName, columnIndex) => {
    const cellValue = toText(row[columnIndex]);
    if (!fieldName || !cellValue) {
      return;
    }

    if (!record[fieldName]) {
      record[fieldName] = cellValue;
    }
  });

  return record;
}

function resolveLetter(record) {
  const directLetter = pickValue(record, fieldAliases.letter);
  if (directLetter) {
    return directLetter.charAt(0).toLowerCase();
  }

  const abbreviation = pickValue(record, fieldAliases.abbreviation);
  if (abbreviation) {
    return abbreviation.charAt(0).toLowerCase();
  }

  const term = pickValue(record, fieldAliases.term);
  if (term) {
    return term.charAt(0).toLowerCase();
  }

  return "";
}

function rowsToTopic(sheetName, rows) {
  if (!rows.length) {
    return null;
  }

  const headerRowIndex = findHeaderRowIndex(rows);
  const mapping = headerRowIndex >= 0 ? buildRowMapping(rows[headerRowIndex]) : buildPositionalMapping(rows[0].length);
  const dataRows = headerRowIndex >= 0 ? rows.slice(headerRowIndex + 1) : rows;
  const cards = dataRows
    .map((row, index) => {
      const record = buildRecordFromRow(row, mapping);
      const abbreviation = pickValue(record, fieldAliases.abbreviation);
      const term = pickValue(record, fieldAliases.term);
      const definition = pickValue(record, fieldAliases.definition);
      const casual = pickValue(record, fieldAliases.casual);
      const example = pickValue(record, fieldAliases.example);
      const technical = pickValue(record, fieldAliases.technical);
      const graphType = pickValue(record, fieldAliases.graphType);
      const graphTitle = pickValue(record, fieldAliases.graphTitle);
      const graphLabels = pickValue(record, fieldAliases.graphLabels);
      const graphValues = pickValue(record, fieldAliases.graphValues);
      const explanation = pickValue(record, fieldAliases.explanation);
      const story = pickValue(record, fieldAliases.story);

      if (
        !abbreviation &&
        !term &&
        !definition &&
        !casual &&
        !example &&
        !technical &&
        !graphType &&
        !graphTitle &&
        !graphLabels &&
        !graphValues &&
        !explanation &&
        !story
      ) {
        return null;
      }

      return {
        letter: resolveLetter(record),
        abbreviation,
        term,
        definition: definition || casual || explanation || technical || example || story,
        casual: casual || definition || explanation || technical,
        example: example || story || definition || explanation,
        technical: technical || explanation || definition,
        graphType,
        graphTitle,
        graphLabels,
        graphValues,
        _rowIndex: index,
      };
    })
    .filter(Boolean);

  if (!cards.length) {
    return null;
  }

  return {
    name: sheetName,
    cards,
  };
}

function parseXml(xmlText) {
  const parser = new DOMParser();
  const documentNode = parser.parseFromString(xmlText, "application/xml");
  if (documentNode.querySelector("parsererror")) {
    throw new Error("The workbook contains XML that could not be read.");
  }
  return documentNode;
}

function findEndOfCentralDirectory(bytes) {
  for (let index = bytes.length - 22; index >= 0; index -= 1) {
    if (
      bytes[index] === 0x50 &&
      bytes[index + 1] === 0x4b &&
      bytes[index + 2] === 0x05 &&
      bytes[index + 3] === 0x06
    ) {
      return index;
    }
  }

  return -1;
}

function readZipEntries(arrayBuffer) {
  const bytes = new Uint8Array(arrayBuffer);
  const view = new DataView(arrayBuffer);
  const endOfCentralDirectory = findEndOfCentralDirectory(bytes);

  if (endOfCentralDirectory === -1) {
    throw new Error("That file does not look like a valid .xlsx workbook.");
  }

  const entryCount = view.getUint16(endOfCentralDirectory + 10, true);
  const centralDirectoryOffset = view.getUint32(endOfCentralDirectory + 16, true);
  const decoder = new TextDecoder("utf-8");
  const entries = new Map();
  let cursor = centralDirectoryOffset;

  for (let entryIndex = 0; entryIndex < entryCount; entryIndex += 1) {
    if (view.getUint32(cursor, true) !== 0x02014b50) {
      throw new Error("The workbook archive could not be read.");
    }

    const compressionMethod = view.getUint16(cursor + 10, true);
    const compressedSize = view.getUint32(cursor + 20, true);
    const fileNameLength = view.getUint16(cursor + 28, true);
    const extraFieldLength = view.getUint16(cursor + 30, true);
    const commentLength = view.getUint16(cursor + 32, true);
    const localHeaderOffset = view.getUint32(cursor + 42, true);
    const fileNameStart = cursor + 46;
    const fileNameEnd = fileNameStart + fileNameLength;
    const fileName = decoder.decode(bytes.slice(fileNameStart, fileNameEnd));

    entries.set(fileName, {
      compressionMethod,
      compressedSize,
      localHeaderOffset,
    });

    cursor = fileNameEnd + extraFieldLength + commentLength;
  }

  return entries;
}

async function inflateRaw(bytes) {
  if (typeof DecompressionStream === "undefined") {
    throw new Error("This browser needs DecompressionStream support to read .xlsx files.");
  }

  const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("deflate-raw"));
  return new Uint8Array(await new Response(stream).arrayBuffer());
}

async function extractZipEntry(arrayBuffer, entries, entryPath) {
  const entry = entries.get(entryPath);
  if (!entry) {
    return null;
  }

  const bytes = new Uint8Array(arrayBuffer);
  const view = new DataView(arrayBuffer);
  const localHeaderOffset = entry.localHeaderOffset;

  if (view.getUint32(localHeaderOffset, true) !== 0x04034b50) {
    throw new Error("The workbook entry headers could not be read.");
  }

  const fileNameLength = view.getUint16(localHeaderOffset + 26, true);
  const extraFieldLength = view.getUint16(localHeaderOffset + 28, true);
  const dataStart = localHeaderOffset + 30 + fileNameLength + extraFieldLength;
  const compressedBytes = bytes.slice(dataStart, dataStart + entry.compressedSize);

  if (entry.compressionMethod === 0) {
    return compressedBytes;
  }

  if (entry.compressionMethod === 8) {
    return inflateRaw(compressedBytes);
  }

  throw new Error("This workbook uses a ZIP compression method that this template does not support.");
}

async function readEntryText(arrayBuffer, entries, entryPath) {
  const data = await extractZipEntry(arrayBuffer, entries, entryPath);
  if (!data) {
    return "";
  }

  return new TextDecoder("utf-8").decode(data);
}

function resolveZipPath(basePath, targetPath) {
  if (!targetPath) {
    return "";
  }

  if (targetPath.startsWith("/")) {
    return targetPath.slice(1);
  }

  const segments = basePath.split("/");
  segments.pop();

  targetPath.split("/").forEach((segment) => {
    if (!segment || segment === ".") {
      return;
    }

    if (segment === "..") {
      segments.pop();
      return;
    }

    segments.push(segment);
  });

  return segments.join("/");
}

function readSharedStrings(sharedStringsXml) {
  if (!sharedStringsXml) {
    return [];
  }

  const documentNode = parseXml(sharedStringsXml);
  return Array.from(documentNode.getElementsByTagName("si")).map((stringNode) =>
    Array.from(stringNode.getElementsByTagName("t"))
      .map((textNode) => textNode.textContent || "")
      .join(""),
  );
}

function cellReferenceToIndex(reference) {
  const match = String(reference || "").match(/[A-Z]+/i);
  if (!match) {
    return null;
  }

  return match[0]
    .toUpperCase()
    .split("")
    .reduce((total, character) => total * 26 + character.charCodeAt(0) - 64, 0) - 1;
}

function readCellText(cellNode, sharedStrings) {
  const type = cellNode.getAttribute("t");

  if (type === "inlineStr") {
    return Array.from(cellNode.getElementsByTagName("t"))
      .map((textNode) => textNode.textContent || "")
      .join("");
  }

  const valueNode = cellNode.getElementsByTagName("v")[0];
  const rawValue = valueNode?.textContent || "";

  if (type === "s") {
    return sharedStrings[Number(rawValue)] || "";
  }

  if (type === "b") {
    return rawValue === "1" ? "TRUE" : "FALSE";
  }

  return rawValue;
}

function readWorksheetRows(worksheetXml, sharedStrings) {
  const documentNode = parseXml(worksheetXml);
  const rowNodes = Array.from(documentNode.getElementsByTagName("row"));

  return rowNodes
    .map((rowNode) => {
      const values = [];
      Array.from(rowNode.getElementsByTagName("c")).forEach((cellNode, fallbackIndex) => {
        const referenceIndex = cellReferenceToIndex(cellNode.getAttribute("r"));
        const columnIndex = referenceIndex === null ? fallbackIndex : referenceIndex;
        values[columnIndex] = toText(readCellText(cellNode, sharedStrings));
      });
      return values;
    })
    .filter((row) => row.some((value) => value));
}

async function parseWorkbookTopics(arrayBuffer) {
  const entries = readZipEntries(arrayBuffer);
  const workbookXml = await readEntryText(arrayBuffer, entries, "xl/workbook.xml");
  const workbookRelsXml = await readEntryText(arrayBuffer, entries, "xl/_rels/workbook.xml.rels");

  if (!workbookXml || !workbookRelsXml) {
    throw new Error("The workbook is missing its main sheet definitions.");
  }

  const workbookDocument = parseXml(workbookXml);
  const workbookRelsDocument = parseXml(workbookRelsXml);
  const relationshipTargets = new Map(
    Array.from(workbookRelsDocument.getElementsByTagName("Relationship")).map((relationshipNode) => [
      relationshipNode.getAttribute("Id"),
      relationshipNode.getAttribute("Target"),
    ]),
  );

  const sharedStrings = readSharedStrings(await readEntryText(arrayBuffer, entries, "xl/sharedStrings.xml"));
  const workbookSheets = Array.from(workbookDocument.getElementsByTagName("sheet")).map((sheetNode) => ({
    name: sheetNode.getAttribute("name") || "Topic",
    relationshipId: sheetNode.getAttribute("r:id") || "",
  }));

  const parsedTopics = [];

  for (const sheet of workbookSheets) {
    const targetPath = relationshipTargets.get(sheet.relationshipId);
    if (!targetPath) {
      continue;
    }

    const worksheetPath = resolveZipPath("xl/workbook.xml", targetPath);
    const worksheetXml = await readEntryText(arrayBuffer, entries, worksheetPath);
    if (!worksheetXml) {
      continue;
    }

    const rows = readWorksheetRows(worksheetXml, sharedStrings);
    const topic = rowsToTopic(sheet.name, rows);
    if (topic) {
      parsedTopics.push(topic);
    }
  }

  return parsedTopics;
}

async function handleWorkbookUpload(event) {
  const [file] = Array.from(event.target.files || []);
  if (!file) {
    return;
  }

  try {
    const workbookBuffer = await file.arrayBuffer();
    const workbookTopics = await parseWorkbookTopics(workbookBuffer);
    setTopics(workbookTopics, "excel loaded");
  } catch (error) {
    setStatus(error.message || "That workbook could not be read.", "error");
  }
}

async function maybeLoadWorkbookFromQuery() {
  const params = new URLSearchParams(window.location.search);
  const workbookPath = params.get("workbook") || (params.get("sample") === "1" ? "sample_flashcards.xlsx" : "");

  if (!workbookPath) {
    return;
  }

  try {
    const response = await fetch(workbookPath);
    if (!response.ok) {
      throw new Error("The requested workbook could not be loaded automatically.");
    }

    const workbookTopics = await parseWorkbookTopics(await response.arrayBuffer());
    setTopics(workbookTopics, "excel loaded");
  } catch (error) {
    setStatus(error.message || "The requested workbook could not be loaded automatically.", "error");
  }
}

async function init() {
  setTopics(cloneDefaultTopics());
  clearStatus();
  elements.workbookInput.addEventListener("change", handleWorkbookUpload);
  window.addEventListener("scroll", scheduleIndexScrollSync, { passive: true });
  window.addEventListener("resize", scheduleIndexScrollSync);
  await maybeLoadWorkbookFromQuery();
}

init();
