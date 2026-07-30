import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel3FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel3FlatComponentChunk33

end RHP2Bridge
