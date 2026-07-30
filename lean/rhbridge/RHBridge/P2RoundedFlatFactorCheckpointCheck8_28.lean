import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel8FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel8FlatComponentChunk28

end RHP2Bridge
