import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel6FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel6FlatComponentChunk28

end RHP2Bridge
