import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel6FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel6FlatComponentChunk46

end RHP2Bridge
