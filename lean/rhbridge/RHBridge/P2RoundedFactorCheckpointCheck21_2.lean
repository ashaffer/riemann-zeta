import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk2 :
    P2RoundedFactorCheckpointData.panel21Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix8_eq :
    P2RoundedFactorCheckpointData.panel21Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk2.1

theorem panel21Prefix9_eq :
    P2RoundedFactorCheckpointData.panel21Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk2.2.1

theorem panel21Prefix10_eq :
    P2RoundedFactorCheckpointData.panel21Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk2.2.2.1

theorem panel21Prefix11_eq :
    P2RoundedFactorCheckpointData.panel21Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk2.2.2.2

end RHP2Bridge
