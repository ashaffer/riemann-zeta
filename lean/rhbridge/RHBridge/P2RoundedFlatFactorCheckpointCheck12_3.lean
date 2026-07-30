import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel12FlatEven3 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven3 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel12FlatComponentChunk3

end RHP2Bridge
