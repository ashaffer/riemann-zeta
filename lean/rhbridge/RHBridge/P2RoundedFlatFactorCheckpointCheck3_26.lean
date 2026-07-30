import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel3FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel3FlatComponentChunk26

end RHP2Bridge
