import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk2 :
    P2RoundedFactorCheckpointData.panel24Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix8_eq :
    P2RoundedFactorCheckpointData.panel24Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk2.1

theorem panel24Prefix9_eq :
    P2RoundedFactorCheckpointData.panel24Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk2.2.1

theorem panel24Prefix10_eq :
    P2RoundedFactorCheckpointData.panel24Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk2.2.2.1

theorem panel24Prefix11_eq :
    P2RoundedFactorCheckpointData.panel24Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk2.2.2.2

end RHP2Bridge
