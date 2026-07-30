import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel9FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel9FlatComponentChunk46

end RHP2Bridge
