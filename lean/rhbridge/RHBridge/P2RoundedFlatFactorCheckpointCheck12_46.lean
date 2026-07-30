import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel12FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel12FlatComponentChunk46

end RHP2Bridge
