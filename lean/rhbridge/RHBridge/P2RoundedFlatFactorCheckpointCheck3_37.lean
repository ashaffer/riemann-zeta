import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel3FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel3FlatComponentChunk37

end RHP2Bridge
