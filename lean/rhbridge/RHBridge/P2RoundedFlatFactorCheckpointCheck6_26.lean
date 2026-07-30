import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel6FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel6FlatComponentChunk26

end RHP2Bridge
