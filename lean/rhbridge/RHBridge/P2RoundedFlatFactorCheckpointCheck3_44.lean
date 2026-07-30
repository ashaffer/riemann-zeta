import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel3FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel3FlatComponentChunk44

end RHP2Bridge
