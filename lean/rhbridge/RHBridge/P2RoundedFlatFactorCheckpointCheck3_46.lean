import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel3FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel3FlatComponentChunk46

end RHP2Bridge
