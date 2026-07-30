import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel12FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel12FlatComponentChunk43

end RHP2Bridge
