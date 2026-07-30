import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel10FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel10FlatComponentChunk42

end RHP2Bridge
