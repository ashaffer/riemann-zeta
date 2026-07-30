import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk1 :
    P2RoundedFactorCheckpointData.panel11Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix4_eq :
    P2RoundedFactorCheckpointData.panel11Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk1.1

theorem panel11Prefix5_eq :
    P2RoundedFactorCheckpointData.panel11Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk1.2.1

theorem panel11Prefix6_eq :
    P2RoundedFactorCheckpointData.panel11Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk1.2.2.1

theorem panel11Prefix7_eq :
    P2RoundedFactorCheckpointData.panel11Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk1.2.2.2

end RHP2Bridge
