import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel31FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel31FlatComponentChunk35

end RHP2Bridge
