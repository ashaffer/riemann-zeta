import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk3 :
    P2RoundedFactorCheckpointData.panel11Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix12_eq :
    P2RoundedFactorCheckpointData.panel11Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk3.1

theorem panel11Prefix13_eq :
    P2RoundedFactorCheckpointData.panel11Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk3.2.1

theorem panel11Prefix14_eq :
    P2RoundedFactorCheckpointData.panel11Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk3.2.2.1

theorem panel11Prefix15_eq :
    P2RoundedFactorCheckpointData.panel11Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk3.2.2.2

end RHP2Bridge
