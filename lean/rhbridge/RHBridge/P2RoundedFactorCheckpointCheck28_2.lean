import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk2 :
    P2RoundedFactorCheckpointData.panel28Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix8_eq :
    P2RoundedFactorCheckpointData.panel28Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk2.1

theorem panel28Prefix9_eq :
    P2RoundedFactorCheckpointData.panel28Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk2.2.1

theorem panel28Prefix10_eq :
    P2RoundedFactorCheckpointData.panel28Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk2.2.2.1

theorem panel28Prefix11_eq :
    P2RoundedFactorCheckpointData.panel28Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk2.2.2.2

end RHP2Bridge
