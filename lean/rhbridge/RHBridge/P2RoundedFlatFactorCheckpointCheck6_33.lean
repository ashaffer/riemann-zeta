import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel6FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel6FlatComponentChunk33

end RHP2Bridge
