import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel12FlatEven22 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven22 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel12FlatComponentChunk22

end RHP2Bridge
