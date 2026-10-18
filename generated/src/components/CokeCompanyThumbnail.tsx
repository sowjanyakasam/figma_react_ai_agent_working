import React from "react";
import artworkUrl from "../assets/coke-company-thumbnail.png";

export function CokeCompanyThumbnail() {
  return (
    <main
      aria-label="The Coca-Cola Company"
      style={{
        aspectRatio: "2 / 1",
        background: "linear-gradient(110deg, #ed1c2b 0%, #c8102e 48%, #8b0017 100%)",
        overflow: "hidden",
        width: "100%",
      }}
    >
      <img
        alt="The Coca-Cola Company"
        src={artworkUrl}
        style={{ display: "block", height: "100%", objectFit: "contain", width: "100%" }}
      />
    </main>
  );
}
