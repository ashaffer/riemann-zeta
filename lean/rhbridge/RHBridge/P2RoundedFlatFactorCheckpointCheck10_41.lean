import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel10FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel10FlatComponentChunk41

end RHP2Bridge
