import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk19 :
    P2RoundedFactorCheckpointData.panel23FlatEven19 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel23FlatEven19_eq :
    P2RoundedFactorCheckpointData.panel23FlatEven19 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  exact panel23FlatComponentChunk19

end RHP2Bridge
