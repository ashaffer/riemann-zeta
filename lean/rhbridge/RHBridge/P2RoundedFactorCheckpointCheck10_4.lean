import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk4 :
    P2RoundedFactorCheckpointData.panel10Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix16_eq :
    P2RoundedFactorCheckpointData.panel10Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk4.1

theorem panel10Prefix17_eq :
    P2RoundedFactorCheckpointData.panel10Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk4.2.1

theorem panel10Prefix18_eq :
    P2RoundedFactorCheckpointData.panel10Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk4.2.2.1

theorem panel10Prefix19_eq :
    P2RoundedFactorCheckpointData.panel10Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk4.2.2.2

end RHP2Bridge
