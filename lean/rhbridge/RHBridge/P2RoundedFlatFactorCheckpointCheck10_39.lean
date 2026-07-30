import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel10FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel10FlatComponentChunk39

end RHP2Bridge
