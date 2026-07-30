import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk4 :
    P2RoundedFactorCheckpointData.panel12Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix16_eq :
    P2RoundedFactorCheckpointData.panel12Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk4.1

theorem panel12Prefix17_eq :
    P2RoundedFactorCheckpointData.panel12Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk4.2.1

theorem panel12Prefix18_eq :
    P2RoundedFactorCheckpointData.panel12Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk4.2.2.1

theorem panel12Prefix19_eq :
    P2RoundedFactorCheckpointData.panel12Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk4.2.2.2

end RHP2Bridge
