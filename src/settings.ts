import { RGB } from "./common";

export enum ClusteringColorSpace {
    RGB = 0,
    HSL = 1,
    LAB = 2,
}

export class Settings {
    public kMeansNrOfClusters: number = 16;
    public kMeansMinDeltaDifference: number = 1;
    public kMeansClusteringColorSpace: ClusteringColorSpace = ClusteringColorSpace.RGB;

    public kMeansColorRestrictions: Array<RGB | string> = [];

    public colorAliases: { [key: string]: RGB } = {};

    public narrowPixelStripCleanupRuns: number = 3; // 3 seems like a good compromise between removing enough narrow pixel strips to convergence. This fixes e.g. https://i.imgur.com/dz4ANz1.png

    public removeFacetsSmallerThanNrOfPoints: number = 20;
    public removeFacetsFromLargeToSmall: boolean = true;
    public maximumNumberOfFacets: number = Number.MAX_VALUE;

    public nrOfTimesToHalveBorderSegments: number = 2;

    public resizeImageIfTooLarge: boolean = true;
    public resizeImageWidth: number = 2000;
    public resizeImageHeight: number = 2000;

    public randomSeed: number = new Date().getTime();
}
