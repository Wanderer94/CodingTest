function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let bridge = new Array(bridge_length).fill(0);
    let bridgeWeight = 0;

    while (truck_weights.length > 0 || bridgeWeight > 0) {
        time++;

        // 다리에서 트럭을 내림
        bridgeWeight -= bridge.shift();

        // 다리에 트럭을 올릴 수 있는지 확인
        if (truck_weights.length > 0 && bridgeWeight + truck_weights[0] <= weight) {
            let truck = truck_weights.shift();
            bridge.push(truck);
            bridgeWeight += truck;
        } else {
            bridge.push(0);
        }
    }

    return time;
}
