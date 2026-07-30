import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel10FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel10FlatComponentChunk43

end RHP2Bridge
